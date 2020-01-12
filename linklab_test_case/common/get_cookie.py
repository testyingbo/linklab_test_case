# --*-- coding:utf8 --*--
# 获取浏览器的cookie
import selenium.webdriver
from linklab_test_case.action.web_service import *


def get_cookie(driver, linklab_url):
    # cookie = [item["name"] + "=" + item["value"] for item in self._driver.get_cookies()]
    cookie = []
    for item in driver.get_cookies():
        cookie.append(item["name"] + "=" + item["value"])
    cookiestr = ';'.join(item for item in cookie)
    return cookiestr
