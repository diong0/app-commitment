from google_play_scraper import Sort, reviews
import csv
import openpyxl
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from lxml import etree
from datetime import datetime
import jieba
import re

def load_stopwords(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        stopwords = set(line.strip() for line in file)
    return stopwords

def remove_stopwords(words, stopwords):
    return [word for word in words if word not in stopwords]

def fetch_reviews(appid, maxDataSize):
    result = []
    continuation_token = None
    while len(result) < maxDataSize:
        count = min(100, maxDataSize - len(result))  # 每次请求最多100条
        reviews_chunk, continuation_token = reviews(
            appid,
            lang='zh',
            country='cn',
            sort=Sort.NEWEST,
            count=count,
            continuation_token=continuation_token
        )
        result.extend(reviews_chunk)
        if not continuation_token:
            break  # 如果没有更多数据，退出循环
    return result

def scrape_google_play_reviews(appname):
    stopwords = load_stopwords('stop.txt')
    chromedriver_path = r"D:\anaconda\chromedriver.exe"
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service)
    driver.get("https://play.google.com/store/apps")
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
            })
          """
    })
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//*[@id="kO001e"]/header/nav/div/div[1]/button').click()
    driver.find_element(By.XPATH, '//*[@id="kO001e"]/header/nav/c-wiz/div/div/label/input').send_keys(appname)
    driver.find_element(By.XPATH, '//*[@id="kO001e"]/header/nav/c-wiz/div/div/label/input').send_keys(Keys.ENTER)
    sleep(2)
    page_source = driver.page_source
    html = etree.HTML(page_source)
    app_link_xpath = '//a[@class="Qfxief"]'
    app_elements = html.xpath(app_link_xpath)
    package_name = None

    if app_elements:
        app_href = app_elements[0].get('href')
        if app_href and 'id=' in app_href:
            package_name = app_href.split('id=')[-1]

    driver.quit()

    if not package_name:
        return []

    appid = package_name
    maxDataSize = 300
    result = fetch_reviews(appid, maxDataSize)

    data_list = []
    comment_data = []
    max_length = 100
    for data in result:
        name = data.get('userName')
        content = data.get('content')
        score = data.get('score')
        at = data.get('at')
        appversion = data.get('appVersion')

        if isinstance(at, datetime):
            at = at.strftime("%Y/%m/%d")

        re_content = re.sub(r'[^\w\s]', '', content)
        re_content = re_content.replace('\n', '')
        re_content = re_content.replace(' ', '')
        if len(content) > max_length:
            content = content[:max_length] + "..."
        text = jieba.lcut(re_content)
        filtered_text = remove_stopwords(text, stopwords)

        data_dict = {
            '评论ID': name,
            '评论内容': content,
            '评论评分': score,
            '评论时间': at,
            '评论版本': appversion
        }
        data_list.append(data_dict)
        comment_data.append([str(name), appname, at, '谷歌', appversion, content, score, [filtered_text]])

    '''
    if data_list:
        with open(f'{appname}.csv', 'w', encoding='utf-8-sig', newline='') as f:
            title = data_list[0].keys()
            writer = csv.DictWriter(f, title)
            writer.writeheader()
            writer.writerows(data_list)
        print('csv文件写入完成')
    else:
        print('没有获取到数据')
    '''

    return comment_data

# 调用示例
# comment_data = scrape_google_play_reviews('YourAppName')
