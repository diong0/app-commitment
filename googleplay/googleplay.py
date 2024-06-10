from google_play_scraper import Sort, reviews
import csv
import openpyxl
from openpyxl.utils import get_column_letter
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from lxml import etree  # 导入lxml库中的etree模块
from datetime import datetime

appname = '抖音'
# 寻找包名
# 设置ChromeDriver的路径
chromedriver_path = r"D:\anaconda\chromedriver.exe"

# 创建ChromeDriver服务对象
service = Service(chromedriver_path)

# 创建Chrome浏览器实例
driver = webdriver.Chrome(service=service)

# 打开一个网页
driver.get("https://play.google.com/store/apps")

# 在浏览器执行JavaScript代码，用于欺骗检测机制，隐藏webdriver属性
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
            })
          """
})
# 等待页面加载
driver.implicitly_wait(10)  # 隐式等待，最多等10秒



driver.find_element(By.XPATH, '//*[@id="kO001e"]/header/nav/div/div[1]/button').click()
driver.find_element(By.XPATH, '//*[@id="kO001e"]/header/nav/c-wiz/div/div/label/input').send_keys(appname)
driver.find_element(By.XPATH, '//*[@id="kO001e"]/header/nav/c-wiz/div/div/label/input').send_keys(Keys.ENTER)
sleep(2)
# 提取搜索结果的包名
page_source = driver.page_source
html = etree.HTML(page_source)

app_link_xpath = '//a[@class="Qfxief"]'
app_elements = html.xpath(app_link_xpath)
package_name = None

if app_elements:
    app_href = app_elements[0].get('href')
    print(f"找到的链接: {app_href}")  # 调试信息
    if app_href and 'id=' in app_href:
        package_name = app_href.split('id=')[-1]

if package_name:
    print(f"应用包名: {package_name}")
else:
    print("未找到应用包名")

appid = package_name
maxDataSize = 300

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

result = fetch_reviews(appid, maxDataSize)

data_list = []
for data in result:
    name = data.get('userName')
    content = data.get('content')
    score = data.get('score')
    at = data.get('at')
    appversion = data.get('appVersion')

    # 格式化日期
    if isinstance(at, datetime):
        at = at.strftime("%Y/%m/%d")

    data_dict = {
        '评论ID': name,
        '评论内容': content,
        '评论评分': score,
        '评论时间': at,
        '评论版本': appversion
    }
    data_list.append(data_dict)

if data_list:
    with open(f'{appname}.csv', 'w', encoding='utf-8-sig', newline='') as f:
        title = data_list[0].keys()
        writer = csv.DictWriter(f, title)
        writer.writeheader()
        writer.writerows(data_list)
    print('csv文件写入完成')
else:
    print('没有获取到数据')
