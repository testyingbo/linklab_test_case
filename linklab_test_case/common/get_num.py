# --*-- coding:utf8 --*--
# 获取浏览器的cookie
import selenium.webdriver
import requests
import json


def get_num(driver, buzhou, url1):
    cookie = []
    for item in driver.get_cookies():
        cookie.append(item["name"] + "=" + item["value"])
    cookiestr = ';'.join(item for item in cookie)
    url = url1
    headers = {'cookie': cookiestr}
    response = requests.get(url=url, headers=headers)
    res1 = json.loads(response.text)
    res2 = res1["data"]
    return res2[buzhou]




