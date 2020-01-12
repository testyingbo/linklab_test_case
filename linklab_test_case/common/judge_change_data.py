#!/usr/bin/env python
# coding=utf8
# 对比修改数据前后数据是否一致 和质疑记录是否存在

import unittest
import requests
import json
import time
from selenium import webdriver
import linklab_test_case.common.get_cookie as get_cookie


# 默认项目ID为自动化测试项目的ID
def judge_change_data(driver, url, project_id='583447510010155008'):
    url_str = str(driver.current_url)
    subject_id = url_str[-47:-28]
    form_id = url_str[65:84]
    new_url = url + '/management/proxy/survey/collecting/' + project_id+'/' + form_id+'/?subjectId='+subject_id
    cookie = get_cookie.get_cookie(driver, url_str)
    headers = {'cookie': cookie}
    response = requests.get(url=new_url, headers=headers)
    res1 = json.loads(response.text)
    res2 = res1['data']['subjectForm']['answers']
    data_list = []
    for i in res2:
        if 'value' in i:
            data_list.append(i['value'])
        elif 'selectOptions' in i:
            for k in i['selectOptions']:
                data_list.append(k['valueCode'])
        elif 'result' in i:
            data_list.append(i['result'])
        elif 'score' in i:
            data_list.append(i['score'])
        elif 'calculate' in i:
            data_list.append(i['calculate'])
        elif 'city' in i:
            data_list.append(i['city'])
        elif 'text' in i:
            data_list.append(i['text'])
        elif 'selectOption' in i:
            data_list.append(i['selectOption']['valueCode'])
    return data_list


# 默认项目ID为自动化测试项目的ID
def question_history(driver, url, project_id='583447510010155008'):
    url_str = str(driver.current_url)
    subject_id = url_str[-47:-28]
    form_id = url_str[65:84]
    new_url = url + '/management/proxy/survey/collecting/' + project_id+'/' + form_id+'/?subjectId='+subject_id
    cookie = get_cookie.get_cookie(driver, url_str)
    headers = {'cookie': cookie}
    response = requests.get(url=new_url, headers=headers)
    res1 = json.loads(response.text)
    res2 = res1['data']['qcs']
    if res2 is None:
        return False
    else:
        for i in res2:
            if i['status'] == 1:
                return True
                break
            else:
                return False


