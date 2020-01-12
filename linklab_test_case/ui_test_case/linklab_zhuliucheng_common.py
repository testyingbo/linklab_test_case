#!/usr/bin/env python
# coding=utf-8
import unittest
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from linklab_test_case.action.login import *
from linklab_test_case.common.commit_presence import *
from linklab_test_case.common.enter_subform import *
from linklab_test_case.common.get_num import *


# 创建案例并填写
def creat_subject(self, position):
    login(self._driver, self._linklab_url, TEST_JYB_ONLINE)
    self._driver.get(self._linklab_url + '/project/user/#/')
    wait_and_find_elements_by_link_text(self._driver, '进入项目')[position].click()
    wait_and_find_elements_by_class_name(self._driver, 'navItem-title')[2].click()
    wait_and_find_elements_by_link_text(self._driver, '新增案例')[0].click()
    time.sleep(1)
    wait_and_find_elements_by_class_name(self._driver, 'ant-select-enabled')[1].click()
    time.sleep(1)
    wait_and_find_elements_by_class_name(self._driver, 'ant-select-dropdown-menu-item')[0].click()
    wait_and_find_element_by_xpath(self._driver,
                                        '/html/body/div[2]/div/div[2]/div/div[1]/div[3]/div/button[2]').click()
    subject_name = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    all_hand = self._driver.window_handles
    self._driver.switch_to.window(all_hand[-1])
    wait_and_find_element_by_tag_name(self._driver, 'input').send_keys(subject_name)
    wait_and_find_elements_by_class_name(self._driver, 'modal-confirm')[1].click()
    commit_presence(self._driver, "新建案例")


# 提交表单
def submit(self, position):
    login(self._driver, self._linklab_url, TEST_JYB_ONLINE)
    self._driver.get(self._linklab_url + '/project/user/#/')
    wait_and_find_elements_by_link_text(self._driver, '进入项目')[position].click()
    wait_and_find_elements_by_class_name(self._driver, 'navItem-title')[2].click()
    wait_and_find_elements_by_class_name(self._driver, 'collect_modules')[0].click()
    all_hand = self._driver.window_handles
    self._driver.switch_to.window(all_hand[-1])
    time.sleep(1)
    wait_and_find_elements_by_class_name(self._driver, "ant-tree-switcher")[2].click()
    time.sleep(1)
    wait_and_find_elements_by_class_name(self._driver, "formNav-title-pathname")[2].click()
    wait_and_find_elements_by_class_name(self._driver, "defLabel")[5].click()
    wait_and_find_elements_by_class_name(self._driver, "defLabel")[7].click()
    wait_and_find_elements_by_class_name(self._driver, "modal-confirm")[0].click()
    time.sleep(1)
    wait_and_find_elements_by_class_name(self._driver, "modal-confirm")[1].click()
    commit_presence(self._driver, '单选题')


def SDV(self, position, url):
    login(self._driver, self._linklab_url, CRA_ONLINE)
    time.sleep(1)
    url = url
    amount = int(get_num(self._driver, "sdv", url))
    self._driver.get(self._linklab_url + '/project/user/#/')
    wait_and_find_elements_by_link_text(self._driver, '进入项目')[position].click()
    wait_and_find_elements_by_class_name(self._driver, 'navItem-title')[1].click()
    time.sleep(1)
    num = len(wait_and_find_elements_by_class_name(self._driver, 'ant-table-row-level-0'))
    num = num / 2 + 1
    wait_and_find_elements_by_class_name(self._driver, 'ant-table-row-level-0')[num].click()
    all_hand = self._driver.window_handles
    self._driver.switch_to.window(all_hand[-1])
    wait_and_find_element_by_class_name(self._driver, 'btn-primary').click()
    wait_and_find_elements_by_class_name(self._driver, 'ant-btn')[0].click()
    wait_and_find_elements_by_class_name(self._driver, 'ant-btn')[2].click()
    wait_and_find_elements_by_class_name(self._driver, 'model-btn')[1].click()
    time.sleep(2)
    self._driver.refresh()
    time.sleep(1)
    try:
        amount1 = int(get_num(self._driver, "sdv", url))
        if amount == (amount1 + 1):
            print "SDV成功"
        else:
            print "SDV失败"

    except ValueError:
        print "SDV失败"


def checked(self, position, url):
    login(self._driver, self._linklab_url, TEST_JYB_ONLINE)
    time.sleep(1)
    url = url
    amount = int(get_num(self._driver, "check", url))
    time.sleep(1)
    self._driver.get(self._linklab_url + '/project/user/#/')
    wait_and_find_elements_by_link_text(self._driver, '进入项目')[position].click()
    wait_and_find_elements_by_class_name(self._driver, 'navItem-title')[1].click()
    wait_and_find_elements_by_xpath(self._driver, "//li[@value='check']")[0].click()
    time.sleep(1)
    self._driver.refresh()
    num = len(wait_and_find_elements_by_class_name(self._driver, 'ant-table-row-level-0'))
    num = num/2+1
    wait_and_find_elements_by_class_name(self._driver, 'ant-table-row-level-0')[num].click()
    all_hand = self._driver.window_handles
    self._driver.switch_to.window(all_hand[-1])
    wait_and_find_elements_by_class_name(self._driver, 'btn-primary')[1].click()
    wait_and_find_elements_by_class_name(self._driver, 'ant-btn')[0].click()
    wait_and_find_elements_by_class_name(self._driver, 'ant-btn')[2].click()
    wait_and_find_elements_by_class_name(self._driver, 'model-btn')[1].click()
    time.sleep(2)
    self._driver.refresh()
    time.sleep(1)
    try:
        amount1 = int(get_num(self._driver, "check", url))
        if amount == (amount1 + 1):
            print "核查成功"
        else:
            "核查失败"
    except ValueError:
        print "核查失败"


def sign(self, position, url):
    login(self._driver, self._linklab_url, TEST_JYB_ONLINE)
    time.sleep(1)
    url = url
    amount = int(get_num(self._driver, "sign", url))
    self._driver.get(self._linklab_url + '/project/user/#/')
    wait_and_find_elements_by_link_text(self._driver, '进入项目')[position].click()
    wait_and_find_elements_by_class_name(self._driver, 'navItem-title')[1].click()
    time.sleep(1)
    wait_and_find_element_by_xpath(self._driver, "//li[@value='sign']").click()
    self._driver.refresh()
    wait_and_find_elements_by_class_name(self._driver, 'ant-checkbox-input')[0].click()
    time.sleep(1)
    wait_and_find_element_by_class_name(self._driver, 'ant-btn-default').click()
    wait_and_find_element_by_id(self._driver, 'title-input-id').send_keys(TEST_JYB_ONLINE['password'])
    time.sleep(2)
    self._driver.refresh()
    time.sleep(1)
    try:
        amount1 = int(get_num(self._driver, "sign", url))
        if amount == (amount1 + 1):
            print "sign成功"
        else:
            "sign失败"
    except ValueError:
        print "sign失败"


def lock(self, position, url):
    login(self._driver, self._linklab_url, TEST_JYB_ONLINE)
    time.sleep(1)
    amount = int(get_num(self._driver, "lock", url))
    time.sleep(1)
    self._driver.get(self._linklab_url + '/project/user/#/')
    wait_and_find_elements_by_link_text(self._driver, '进入项目')[position].click()
    wait_and_find_elements_by_class_name(self._driver, 'navItem-title')[1].click()
    time.sleep(1)
    wait_and_find_element_by_xpath(self._driver, "//li[@value='lock']").click()
    self._driver.refresh()
    wait_and_find_elements_by_class_name(self._driver, 'ant-checkbox-input')[0].click()
    wait_and_find_element_by_class_name(self._driver, 'ant-btn-default').click()
    wait_and_find_element_by_id(self._driver, 'copy-but-id').click()
    self._driver.refresh()
    time.sleep(1)
    try:
        amount1 = int(get_num(self._driver, "lock", url))
        if amount == (amount1 + 1):
            print "锁定成功"
        else:
            "锁定失败"
    except ValueError:
        print "锁定失败"
