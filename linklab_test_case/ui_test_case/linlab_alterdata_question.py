#!/usr/bin/env python
# coding=utf8
# 修改数据和提出质疑UI测试
import unittest
import selenium.webdriver
import linklab_test_case.constants as constans
from linklab_test_case.common.enter_subform import *
from linklab_test_case.action.login import *
from linklab_test_case.action.web_service import *
from linklab_test_case.common.judge_change_data import *


class AlterData(unittest.TestCase):
    url = ''
    driver = None

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.linklab_url = constans.BASE_URL_ONLINE
        self.driver.maximize_window()
        login(self.driver, self.linklab_url, constans.TEST_JYB_ONLINE)

    def tearDown(self):
        self.driver.quit()
        with open('labtest.log', 'a') as lab_file:
            lab_file.write(str(self._resultForDoCleanups) + '\n')

    # 修改所有点位表单的数据
    def test_alter_data(self):
        enter_subform(self.driver, self.linklab_url)
        try:
            wait_and_find_elements_by_class_name(self.driver, "ant-tree-switcher")[2].click()
            time.sleep(1)
            wait_and_find_elements_by_class_name(self.driver, "formNav-title-pathname")[3].click()
            time.sleep(1)
            change_data_before = judge_change_data(self.driver, self.linklab_url)
            self.driver.refresh()
            wait_and_find_elements_by_class_name(self.driver, 'icon-pencil_outline')[0].click()
            wait_and_find_elements_by_class_name(self.driver, "anticon-down")[0].click()
            wait_and_find_elements_by_class_name(self.driver, "defLabel")[3].click()
            wait_and_find_elements_by_class_name(self.driver, 'qc-select')[0].click()
            wait_and_find_element_by_xpath(self.driver, '//*[@id="6471640294281461760"]/div/div[3]/div[2]/div/div[1]/select/option[2]').click()
            wait_and_find_elements_by_class_name(self.driver, 'qcbeizhu')[0].send_keys('test')
            wait_and_find_elements_by_class_name(self.driver, 'qc-btn')[0].click()

            wait_and_find_elements_by_class_name(self.driver, 'icon-pencil_outline')[1].click()
            wait_and_find_elements_by_class_name(self.driver, 'replaceInput')[2].click()
            wait_and_find_elements_by_class_name(self.driver, 'qc-select')[0].click()
            wait_and_find_element_by_xpath(self.driver, '//*[@id="6471640301952843776"]/div/div[3]/div[2]/div/div[1]/select/option[2]').click()
            wait_and_find_elements_by_class_name(self.driver, 'qcbeizhu')[0].send_keys('test')
            wait_and_find_elements_by_class_name(self.driver, 'qc-btn')[0].click()

            wait_and_find_elements_by_class_name(self.driver, 'icon-pencil_outline')[2].click()
            wait_and_find_elements_by_class_name(self.driver, 'opentext-input')[1].send_keys('abc')
            wait_and_find_elements_by_class_name(self.driver, 'qc-select')[0].click()
            wait_and_find_element_by_xpath(self.driver, '//*[@id="6471640311364853760"]/div/div[3]/div[2]/div/div[1]/select/option[2]').click()
            wait_and_find_elements_by_class_name(self.driver, 'qcbeizhu')[0].send_keys('test')
            wait_and_find_elements_by_class_name(self.driver, 'qc-btn')[0].click()

            wait_and_find_elements_by_class_name(self.driver, 'icon-pencil_outline')[3].click()
            wait_and_find_elements_by_class_name(self.driver, 'opentext-input')[2].send_keys(123)
            wait_and_find_elements_by_class_name(self.driver, 'qc-select')[0].click()
            wait_and_find_element_by_xpath(self.driver, '//*[@id="6471640319355011072"]/div/div[3]/div[2]/div/div[1]/select/option[2]').click()
            wait_and_find_elements_by_class_name(self.driver, 'qcbeizhu')[0].send_keys('test')
            wait_and_find_elements_by_class_name(self.driver, 'qc-btn')[0].click()

            wait_and_find_elements_by_class_name(self.driver, 'icon-pencil_outline')[4].click()
            wait_and_find_elements_by_class_name(self.driver, 'time-set-input')[0].click()
            time.sleep(1)
            wait_and_find_elements_by_class_name(self.driver, 'date-now')[0].click()
            wait_and_find_elements_by_class_name(self.driver, 'qc-select')[0].click()
            wait_and_find_element_by_xpath(self.driver, '//*[@id="6471640327261261824"]/div/div[3]/div[2]/div/div[1]/select/option[2]').click()
            wait_and_find_elements_by_class_name(self.driver, 'qcbeizhu')[0].send_keys('test')
            wait_and_find_elements_by_class_name(self.driver, 'qc-btn')[0].click()
            wait_and_find_elements_by_class_name(self.driver, 'btn-primary')[0].click()
            time.sleep(1)
            self.driver.refresh()
            change_data_after = judge_change_data(self.driver, self.linklab_url)
            for item in change_data_before:
                if item in change_data_after:
                    continue
                else:
                    print '修改数据成功'
                    break
                print '修改数据失败'
        except ValueError:
            print '单题修改数据失败'

    # 修改组内数据
    def test_alter_group_data(self):
        enter_subform(self.driver, self.linklab_url)
        try:
            wait_and_find_element_by_xpath(self.driver, '//*[@id="caseTree"]/ul/li[2]/span[2]/span/div/div').click()
            wait_and_find_element_by_xpath(self.driver, '//*[@id="caseTree"]/ul/li[2]/ul/li[10]/span[2]/span/div/div').click()
            time.sleep(1)
            change_data_before = judge_change_data(self.driver, self.linklab_url)
            self.driver.refresh()
            wait_and_find_elements_by_class_name(self.driver, 'icon-pencil_outline')[0].click()
            wait_and_find_elements_by_class_name(self.driver, 'selectText')[2].click()
            wait_and_find_elements_by_class_name(self.driver, 'qc-select')[0].click()
            wait_and_find_element_by_xpath(self.driver, '//*[@id="questionRight"]/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div/table/tbody/tr[2]/td[1]/div/div[3]/div[3]/div/div[1]/select/option[2]').click()
            wait_and_find_elements_by_class_name(self.driver, 'qcbeizhu')[0].send_keys('test')
            wait_and_find_elements_by_class_name(self.driver, 'qc-btn')[0].click()

            wait_and_find_elements_by_class_name(self.driver, 'icon-pencil_outline')[2].click()
            wait_and_find_elements_by_class_name(self.driver, 'opentext-input')[0].send_keys('abc')
            wait_and_find_elements_by_class_name(self.driver, 'qc-select')[0].click()
            wait_and_find_element_by_xpath(self.driver, '//*[@id="questionRight"]/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div/table/tbody/tr[2]/td[3]/div/div[3]/div[3]/div/div[1]/select/option[2]').click()
            wait_and_find_elements_by_class_name(self.driver, 'qcbeizhu')[0].send_keys('test')
            wait_and_find_elements_by_class_name(self.driver, 'qc-btn')[0].click()

            wait_and_find_elements_by_class_name(self.driver, 'icon-pencil_outline')[6].click()
            wait_and_find_elements_by_class_name(self.driver, 'ant-cascader-input')[0].click()
            wait_and_find_element_by_xpath(self.driver, "//li[@title='上海市']").click()
            wait_and_find_element_by_xpath(self.driver, "//li[@title='上海辖区']").click()
            wait_and_find_element_by_xpath(self.driver, "//li[@title='宝山区']").click()
            time.sleep(1)
            wait_and_find_elements_by_class_name(self.driver, 'qc-select')[0].click()
            wait_and_find_element_by_xpath(self.driver,'//*[@id="questionRight"]/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div/table/tbody/tr[2]/td[8]/div/div[3]/div[3]/div/div[1]/select/option[2]').click()
            wait_and_find_elements_by_class_name(self.driver, 'qcbeizhu')[0].send_keys('test')
            wait_and_find_elements_by_class_name(self.driver, 'qc-btn')[0].click()
            wait_and_find_elements_by_class_name(self.driver, 'btn-primary')[0].click()
            time.sleep(1)
            self.driver.refresh()
            change_data_after = judge_change_data(self.driver, self.linklab_url)
            for item in change_data_before:
                if item in change_data_after:
                    continue
                else:
                    print '修改组问题答案成功'
                    break
                print '修改组问题答案失败'

        except ValueError:
            print '组内题修改答案失败'

    # 提质疑
    def test_make_question(self):
        enter_subform(self.driver, self.linklab_url)
        try:
            wait_and_find_elements_by_class_name(self.driver, "ant-tree-switcher")[2].click()
            time.sleep(1)
            wait_and_find_elements_by_class_name(self.driver, "formNav-title-pathname")[3].click()
            time.sleep(1)

            wait_and_find_elements_by_class_name(self.driver, 'icon-pointer_outline')[0].click()
            wait_and_find_elements_by_class_name(self.driver, 'qc-input')[0].send_keys(u'质疑测试')
            wait_and_find_elements_by_class_name(self.driver, 'btn-primary')[0].click()

            wait_and_find_elements_by_class_name(self.driver, 'icon-pointer_outline')[4].click()
            wait_and_find_elements_by_class_name(self.driver, 'qc-input')[0].send_keys(u'质疑测试')
            wait_and_find_elements_by_class_name(self.driver, 'btn-primary')[0].click()
            time.sleep(1)

            self.driver.refresh()
            if question_history(self.driver, self.linklab_url):
                print '提出质疑成功'
            else:
                print '提出质疑失败'
        except ValueError:
            print '质疑提出失败'

    def test_close_question(self):
        enter_subform(self.driver, self.linklab_url)
        try:
            wait_and_find_elements_by_class_name(self.driver, 'icon-chatboxes_outline')[0].click()
            time.sleep(1)
            wait_and_find_elements_by_class_name(self.driver, 'over-hidden')[0].click()
            wait_and_find_elements_by_class_name(self.driver, 'ant-input')[0].send_keys('test')
            wait_and_find_elements_by_class_name(self.driver, 'btn-primary')[4].click()
            wait_and_find_elements_by_class_name(self.driver, 'close-qc')[0].click()
            wait_and_find_elements_by_class_name(self.driver, 'btn-danger')[0].click()

            wait_and_find_elements_by_class_name(self.driver, 'icon-chatboxes_outline')[1].click()
            time.sleep(1)
            wait_and_find_elements_by_class_name(self.driver, 'over-hidden')[0].click()
            wait_and_find_elements_by_class_name(self.driver, 'ant-input')[0].send_keys('test')
            wait_and_find_elements_by_class_name(self.driver, 'btn-primary')[4].click()
            wait_and_find_elements_by_class_name(self.driver, 'close-qc')[0].click()
            wait_and_find_elements_by_class_name(self.driver, 'btn-danger')[0].click()
            time.sleep(1)

            self.driver.refresh()
            if question_history(self.driver, self.linklab_url):
                print '关闭质疑失败'
            else:
                print '关闭质疑成功'

        except ValueError:
            print '关闭质疑失败'





















