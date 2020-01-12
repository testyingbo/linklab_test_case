#!/usr/bin/env python
# coding=utf-8
import unittest
import os
import datetime
import random
from selenium.webdriver.common.keys import Keys
from linklab_test_case.action.login import *
from linklab_test_case.action.web_service import *
from linklab_test_case.common.commit_presence import *
from linklab_test_case.common.enter_subform import *


class LinklabTest(unittest.TestCase):
    _driver = None
    _linklab_url = ''

    def setUp(self):  # 设置初始化
        self._linklab_url = BASE_URL_ONLINE
        self._driver = webdriver.Chrome()
        self._driver.maximize_window()
        login(self._driver, self._linklab_url, TEST_JYB_ONLINE)

    def tearDown(self):
        self._driver.quit()
        with open('labtest.log', 'a') as lab_file:
            lab_file.write(str(self._resultForDoCleanups) + '\n')

    # 单选题
    def test_single_choice(self):
        enter_subform(self._driver, self._linklab_url)
        wait_and_find_elements_by_class_name(self._driver, "ant-tree-switcher")[2].click()
        time.sleep(1)
        wait_and_find_elements_by_class_name(self._driver, "formNav-title-pathname")[2].click()
        wait_and_find_elements_by_class_name(self._driver, "defLabel")[5].click()
        wait_and_find_elements_by_class_name(self._driver, "defLabel")[7].click()
        wait_and_find_elements_by_class_name(self._driver, "anticon-down")[0].click()
        wait_and_find_elements_by_class_name(self._driver, "defLabel")[12].click()
        wait_and_find_elements_by_class_name(self._driver, "modal-confirm")[0].click()
        time.sleep(1)
        wait_and_find_elements_by_class_name(self._driver, "modal-confirm")[1].click()
        commit_presence(self._driver, '单选题')

    # 所有点位
    def test_all_subject(self):
        # file_path = "/Users/jin/Desktop/4.png"
        enter_subform(self._driver, self._linklab_url)
        wait_and_find_elements_by_class_name(self._driver, "ant-tree-switcher")[2].click()
        time.sleep(1)
        wait_and_find_elements_by_class_name(self._driver, "formNav-title-pathname")[3].click()
        time.sleep(1)
        wait_and_find_elements_by_class_name(self._driver, "anticon-down")[0].click()
        wait_and_find_elements_by_class_name(self._driver, "defLabel")[2].click()
        wait_and_find_elements_by_class_name(self._driver, "selectText")[0].click()
        wait_and_find_elements_by_class_name(self._driver, "opentext-input")[1].send_keys(u"你好")
        wait_and_find_elements_by_class_name(self._driver, "opentext-input")[2].send_keys("10.2")
        wait_and_find_elements_by_class_name(self._driver, "time-set-input")[0].click()
        time.sleep(1)
        wait_and_find_element_by_class_name(self._driver, "date-now").click()
        wait_and_find_elements_by_class_name(self._driver, "ant-pagination-item-link")[1].click()
        wait_and_find_element_by_xpath(self._driver, "//a[@title='选项2']").click()
        wait_and_find_element_by_class_name(self._driver, "ant-cascader-input").click()
        wait_and_find_element_by_xpath(self._driver, "//li[@title='北京市']").click()
        wait_and_find_element_by_xpath(self._driver, "//li[@title='北京辖区']").click()
        wait_and_find_element_by_xpath(self._driver, "//li[@title='昌平区']").click()
        wait_and_find_elements_by_class_name(self._driver, "modal-confirm")[1].click()
        commit_presence(self._driver,'所有点位')

    # 文件上传
    def test_load_file(self):
        # file_path = "/Users/QA/PycharmProjects/linklab_test/1.png"
        enter_subform(self._driver, self._linklab_url)
        wait_and_find_elements_by_class_name(self._driver, "ant-tree-switcher")[2].click()
        time.sleep(1)
        wait_and_find_elements_by_class_name(self._driver, "formNav-title-pathname")[8].click()
        wait_and_find_elements_by_xpath(self._driver, "//input[@type='file']")[1].send_keys(file_path)
        time.sleep(1)
        wait_and_find_elements_by_class_name(self._driver, "modal-confirm")[0].click()
        time.sleep(1)
        wait_and_find_elements_by_class_name(self._driver, "modal-confirm")[1].click()
        commit_presence(self._driver, '文件题')

    # 打分题
    def test_grade(self):
        enter_subform(self._driver, self._linklab_url)
        time.sleep(1)
        wait_and_find_elements_by_class_name(self._driver, "ant-tree-switcher")[2].click()
        time.sleep(1)
        wait_and_find_elements_by_class_name(self._driver, "formNav-title-pathname")[9].click()
        wait_and_find_element_by_xpath(self._driver, "//a[@title='选项2']").click()
        time.sleep(1)
        wait_and_find_elements_by_class_name(self._driver, "modal-confirm")[0].click()
        time.sleep(1)
        wait_and_find_elements_by_class_name(self._driver, "modal-confirm")[1].click()
        commit_presence(self._driver,'打分题')

    # 地址题
    def test_address(self):
        enter_subform(self._driver, self._linklab_url)
        wait_and_find_elements_by_class_name(self._driver, "ant-tree-switcher")[2].click()
        time.sleep(1)
        wait_and_find_elements_by_class_name(self._driver, "formNav-title-pathname")[10].click()
        wait_and_find_elements_by_class_name(self._driver, "ant-cascader-input")[0].click()
        time.sleep(1)
        wait_and_find_element_by_xpath(self._driver, "//li[@title='北京市']").click()
        wait_and_find_element_by_xpath(self._driver, "//li[@title='北京辖区']").click()
        wait_and_find_element_by_xpath(self._driver, "//li[@title='昌平区']").click()
        wait_and_find_elements_by_class_name(self._driver, "modal-confirm")[1].click()
        commit_presence(self._driver, '地址题')


if __name__ == "__main__":
    unittest.main()