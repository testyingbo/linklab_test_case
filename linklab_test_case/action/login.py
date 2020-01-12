# coding=utf8
import time
import requests
import json
import selenium.webdriver as webdriver
from web_service import *
from linklab_test_case.constants import *
import logging
headers = {}


def login(driver, url, user):
    driver.get(url)
    wait_and_find_element_by_xpath(driver, "//input[@class='form-control error-info zmg-control']").send_keys(user['user_phone'])
    wait_and_find_element_by_xpath(driver, "//input[@class='form-control zmg-control']").send_keys(user['password'])
    wait_and_find_element_by_xpath(driver, "//button[@class='btn login-btn block full-width zmg-login']").click()
    time.sleep(5)


def login_test(username, password):
    r = requests.post(LOGIN_URL_ONLINE, {'username': username, 'password': password})
    if r.status_code != 200:
        raise Exception("Login fail")
    body_json = json.loads(r.text)
    if body_json['status'] != 0:
        raise Exception("Login fail")
    session_id = r.cookies['usercenter.session.id']
    headers['Cookie'] = '' + 'usercenter.session.id={};'.format(session_id)


def login_by_session_test(username, password):
    r = requests.Session()
    r.post(LOGIN_URL_ONLINE, {'username': username, 'password': password})
    session_id = r.cookies['usercenter.session.id']
    r.headers['Cookie'] = '' + 'usercenter.session.id={};'.format(session_id)
    return r


def login_by_session_test_offline(username, password):
    r = requests.Session()
    r.post(LOGIN_URL_TEST, {'username': username, 'password': password})
    session_id = r.cookies['usercenter.session.id']
    r.headers['Cookie'] = '' + 'usercenter.session.id={};'.format(session_id)
    return r


def login_by_session(url, username, password):
    r = requests.Session()
    r.post(url, {'username': username, 'password': password})
    session_id = r.cookies['usercenter.session.id']
    r.headers['Cookie'] = '' + 'usercenter.session.id={};'.format(session_id)
    return r

