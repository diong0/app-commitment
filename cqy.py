from appstore.苹果 import fetch_comments
from huawei.huawei import scrape_app_comments
from googleplay.googleplay import scrape_google_play_reviews
appname = "qq"
comments = scrape_google_play_reviews(appname)
print(comments)
