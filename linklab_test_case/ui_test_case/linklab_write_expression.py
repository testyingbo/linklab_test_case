#!/usr/bin/env python
# coding=utf8
import os
import time
import datetime
import unittest
import selenium.webdriver
import linklab_test_case.action.login as login
import linklab_test_case.constants as constants
from linklab_test_case.action.web_service import *
from linklab_test_case.common.commit_presence import *
from linklab_test_case.common.enter_subform import *


class WriteExpression(unittest.TestCase):
    linklab_url = ''
    driver = None

    def setUp(self):
        self.driver = selenium.webdriver.Chrome()
        self.linklab_url = constants.BASE_URL_ONLINE
        self.driver.maximize_window()
        login.login(self.driver, self.linklab_url, constants.TEST_JYB_ONLINE)

    def tearDown(self):
        self.driver.quit()
        with open('labtest.log', 'a') as lab_file:
            lab_file.write(str(self._resultForDoCleanups) + '\n')

    def test_write_ifresult(self):
        enter_subform(self.driver, self.linklab_url)
        try:
            wait_and_find_elements_by_class_name(self.driver, 'formNav-title-pathname')[3].click()
            wait_and_find_element_by_xpath(self.driver, '//*[@id="caseTree"]/ul/li[3]/ul/li[1]/span[2]/span/div/div').click()
            wait_and_find_elements_by_class_name(self.driver, 'selectText')[2].click()
            wait_and_find_elements_by_class_name(self.driver, 'modal-confirm')[1].click()
        except ValueError:
            print 'ifresult函数填写失败'
        commit_presence_by_xpath(self.driver, 'ifresult函数', '//*[@id="604851781411827712"]/div/div[4]/div/span/i[2]')

    def test_write_answerCheck(self):
        enter_subform(self.driver, self.linklab_url)
        try:
            wait_and_find_elements_by_class_name(self.driver, 'formNav-title-pathname')[3].click()
            wait_and_find_element_by_xpath(self.driver, '//*[@id="caseTree"]/ul/li[3]/ul/li[2]/span[2]/span/div/div').click()
            wait_and_find_elements_by_class_name(self.driver, 'selectText')[0].click()
            wait_and_find_elements_by_class_name(self.driver, 'modal-confirm')[1].click()
        except ValueError:
            print 'answerCheck函数填写失败'
        commit_presence_by_xpath(self.driver, 'answerCkeck函数', '//*[@id="604858191788929024"]/div/div[4]/div/span/i[4]')

    def test_write_timeExpression(self):
        enter_subform(self.driver, self.linklab_url)
        try:
            wait_and_find_elements_by_class_name(self.driver, 'formNav-title-pathname')[3].click()
            wait_and_find_element_by_xpath(self.driver, '//*[@id="caseTree"]/ul/li[3]/ul/li[3]/span[2]/span/div/div').click()
            wait_and_find_element_by_class_name(self.driver, 'time-set-input').click()
            time.sleep(1)
            wait_and_find_element_by_class_name(self.driver, 'date-now').click()
            wait_and_find_elements_by_class_name(self.driver, 'opentext-input')[0].send_keys(1000000000)
            wait_and_find_elements_by_class_name(self.driver, 'opentext-input')[1].send_keys(1000000000)
            wait_and_find_elements_by_class_name(self.driver, 'modal-confirm')[1].click()
        except ValueError:
            print '时间公式填写失败'
        commit_presence_by_xpath(self.driver, '时间公式', '//*[@id="604879795667726336"]/div/div[4]/div/span/i[2]')

    def test_write_math_value(self):
        enter_subform(self.driver, self.linklab_url)
        try:
            wait_and_find_elements_by_class_name(self.driver, 'formNav-title-pathname')[3].click()
            wait_and_find_element_by_xpath(self.driver, '//*[@id="caseTree"]/ul/li[3]/ul/li[4]/span[2]/span/div/div').click()
            time.sleep(1)
            wait_and_find_elements_by_class_name(self.driver, 'form-control')[0].send_keys(3)
            wait_and_find_elements_by_class_name(self.driver, 'form-control')[1].send_keys('2.5')
            wait_and_find_elements_by_class_name(self.driver, 'modal-confirm')[1].click()
        except ValueError:
            print 'math-value填写失败'
        commit_presence_by_xpath(self.driver, 'math-value函数', '//*[@id="607373567696756736"]/div/div[4]/div/span/i[2]')

    def test_write_containsAny(self):
        enter_subform(self.driver, self.linklab_url)
        try:
            wait_and_find_elements_by_class_name(self.driver, 'formNav-title-pathname')[3].click()
            wait_and_find_element_by_xpath(self.driver, '//*[@id="caseTree"]/ul/li[3]/ul/li[5]/span[1]').click()
            time.sleep(1)
            wait_and_find_element_by_xpath(self.driver, '//*[@id="caseTree"]/ul/li[3]/ul/li[5]/ul/li/span[2]/span/div/div').click()
            wait_and_find_elements_by_class_name(self.driver, 'selectText')[0].click()
            wait_and_find_elements_by_class_name(self.driver, 'selectText')[2].click()
            wait_and_find_elements_by_class_name(self.driver, 'modal-confirm')[1].click()
        except ValueError:
            print 'containsAny函数填写失败'
        commit_presence_by_xpath(self.driver, 'containsAny函数', '//*[@id="607379188095586304"]/div/div[4]/div/span/i[2]')

    def test_write_notify(self):
        enter_subform(self.driver, self.linklab_url)
        try:
            wait_and_find_elements_by_class_name(self.driver, 'formNav-title-pathname')[3].click()
            wait_and_find_element_by_xpath(self.driver, '//*[@id="caseTree"]/ul/li[3]/ul/li[6]/span[2]/span/div/div').click()
            wait_and_find_elements_by_class_name(self.driver, 'selectText')[0].click()
            wait_and_find_elements_by_class_name(self.driver, 'modal-confirm')[1].click()
        except ValueError:
            print 'Notify函数填写失败'
        commit_presence_by_xpath(self.driver, 'Notify函数', '//*[@id="626137989230776320"]/div/div[4]/div/span/i[2]')

    def test_freezeForm(self):
        enter_subform(self.driver, self.linklab_url)
        try:
            wait_and_find_elements_by_class_name(self.driver, 'formNav-title-pathname')[3].click()
            wait_and_find_element_by_xpath(self.driver, '//*[@id="caseTree"]/ul/li[3]/ul/li[7]/span[2]/span/div/div').click()
            wait_and_find_elements_by_class_name(self.driver, 'selectText')[0].click()
            wait_and_find_element_by_class_name(self.driver, 'time-set-input').click()
            wait_and_find_element_by_class_name(self.driver, 'date-now').click()
            wait_and_find_elements_by_class_name(self.driver, 'modal-confirm')[1].click()
        except ValueError:
            print 'freezeForm函数填写失败'
        commit_presence_by_xpath(self.driver, 'freezeForm函数', '//*[@id="626140495777087488"]/div/div[4]/div/span/i[2]')

    def test_write_siteProperty_normal(self):
        enter_subform(self.driver, self.linklab_url)
        try:
            wait_and_find_elements_by_class_name(self.driver, 'formNav-title-pathname')[3].click()
            wait_and_find_element_by_xpath(self.driver, '//*[@id="caseTree"]/ul/li[3]/ul/li[9]/span[2]/span/div/div').click()
            wait_and_find_elements_by_class_name(self.driver, 'selectText')[0].click()
            wait_and_find_elements_by_class_name(self.driver, 'opentext-input')[0].send_keys('15')
            wait_and_find_element_by_class_name(self.driver, 'time-set-input').click()
            wait_and_find_element_by_class_name(self.driver, 'date-now').click()
            wait_and_find_elements_by_class_name(self.driver, 'opentext-input')[1].send_keys('120')
            wait_and_find_elements_by_class_name(self.driver, 'modal-confirm')[1].click()
        except ValueError:
            print '实验室正常值函数填写失败'
        commit_presence_by_xpath(self.driver, '实验室正常值函数', '//*[@id="626144714679799808"]/div/div[4]/div/span/i[2]')

    def test_write_parseRegxp(self):
        enter_subform(self.driver, self.linklab_url)
        try:
            wait_and_find_elements_by_class_name(self.driver, 'formNav-title-pathname')[3].click()
            wait_and_find_element_by_xpath(self.driver, '//*[@id="caseTree"]/ul/li[3]/ul/li[10]/span[2]').click()
            time.sleep(1)
            wait_and_find_element_by_class_name(self.driver, 'opentext-input').send_keys('abcdefghijkl')
            wait_and_find_elements_by_class_name(self.driver, 'modal-confirm')[1].click()
        except ValueError:
            print 'parseRegxp函数填写失败'
        commit_presence_by_xpath(self.driver, 'parseRegxp函数', '//*[@id="626148383286513664"]/div/div[4]/div/span/i[2]')

    def test_write_parseInt(self):
        enter_subform(self.driver, self.linklab_url)
        try:
            wait_and_find_elements_by_class_name(self.driver, 'formNav-title-pathname')[3].click()
            wait_and_find_element_by_xpath(self.driver, '//*[@id="caseTree"]/ul/li[3]/ul/li[11]/span[2]').click()
            time.sleep(1)
            wait_and_find_element_by_class_name(self.driver, 'opentext-input').send_keys('101.8')
            wait_and_find_elements_by_class_name(self.driver, 'modal-confirm')[1].click()
        except ValueError:
            print 'parseInt函数填写失败'
        commit_presence_by_xpath(self.driver, 'parseInt函数', '//*[@id="626201550389755904"]/div/div[4]/div/span/i[2]')

    def test_write_now(self):
        enter_subform(self.driver, self.linklab_url)
        try:
            wait_and_find_elements_by_class_name(self.driver, 'formNav-title-pathname')[3].click()
            wait_and_find_element_by_xpath(self.driver, '//*[@id="caseTree"]/ul/li[3]/ul/li[12]/span[2]/span/div/div').click()
            wait_and_find_element_by_class_name(self.driver, 'time-set-input').click()
            time.sleep(1)
            wait_and_find_element_by_class_name(self.driver, 'date-now').click()
            wait_and_find_elements_by_class_name(self.driver, 'modal-confirm')[1].click()
        except ValueError:
            print 'now函数填写失败'
        commit_presence_by_xpath(self.driver, 'now函数', '//*[@id="626201988421894144"]/div/div[4]/div/span/i[4]')

    def test_write_voiid(self):
        enter_subform(self.driver, self.linklab_url)
        try:
            wait_and_find_elements_by_class_name(self.driver, 'formNav-title-pathname')[3].click()
            wait_and_find_element_by_xpath(self.driver, '//*[@id="caseTree"]/ul/li[3]/ul/li[13]/span[2]/span/div/div').click()
            time.sleep(1)
            wait_and_find_elements_by_class_name(self.driver, 'modal-confirm')[1].click()
        except ValueError:
            print 'voiid函数填写失败'
        commit_presence_by_xpath(self.driver, 'voiid函数', '//*[@id="626203282896474112"]/div/div[4]/div/span/i[2]')

    def test_write_numberGenerator(self):
        enter_subform(self.driver, self.linklab_url)
        try:
            wait_and_find_elements_by_class_name(self.driver, 'formNav-title-pathname')[3].click()
            wait_and_find_element_by_xpath(self.driver, '//*[@id="caseTree"]/ul/li[3]/ul/li[14]/span[2]/span/div/div').click()
            wait_and_find_elements_by_class_name(self.driver, 'selectText')[0].click()
            wait_and_find_elements_by_class_name(self.driver, 'modal-confirm')[1].click()
        except ValueError:
            print 'numberGenerator函数填写失败'
        commit_presence_by_xpath(self.driver, 'numberGenerator函数', '//*[@id="626260834789830656"]/div/div[4]/div/span/i[2]')

    def test_write_sae(self):
        enter_subform(self.driver, self.linklab_url)
        try:
            wait_and_find_elements_by_class_name(self.driver, 'formNav-title-pathname')[3].click()
            wait_and_find_element_by_xpath(self.driver, '//*[@id="caseTree"]/ul/li[3]/ul/li[15]/span[2]/span/div/div').click()
            wait_and_find_elements_by_class_name(self.driver, 'selectText')[0].click()
            wait_and_find_elements_by_class_name(self.driver, 'modal-confirm')[1].click()
        except ValueError:
            print 'SAE函数填写失败'
        commit_presence_by_xpath(self.driver, 'SAE函数', '//*[@id="626264092301656064"]/div/div[4]/div/span/i[2]')


if __name__ == '__main__':
    unittest.main()