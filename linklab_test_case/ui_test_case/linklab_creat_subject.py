# --*-- coding:utf8 --*--
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


class CreatSubject(unittest.TestCase):
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

    # 创建案例并填写
    def test_creat_subject(self):
        self.driver.get(self.linklab_url + '/project/user/#/')
        wait_and_find_elements_by_link_text(self.driver, '进入项目')[3].click()
        wait_and_find_elements_by_class_name(self.driver, 'navItem-title')[2].click()
        wait_and_find_elements_by_link_text(self.driver, '新增案例')[0].click()
        time.sleep(1)
        wait_and_find_elements_by_class_name(self.driver, 'ant-select-enabled')[1].click()
        time.sleep(1)
        wait_and_find_elements_by_class_name(self.driver, 'ant-select-dropdown-menu-item')[0].click()
        wait_and_find_element_by_xpath(self.driver,
                                       '/html/body/div[2]/div/div[2]/div/div[1]/div[3]/div/button[2]').click()
        subject_name = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        all_hand = self.driver.window_handles
        self.driver.switch_to.window(all_hand[-1])
        wait_and_find_element_by_tag_name(self.driver, 'input').send_keys(subject_name)
        wait_and_find_elements_by_class_name(self.driver, 'modal-confirm')[1].click()
        commit_presence(self.driver, "新建案例")


    # 填写多选题
    def test_write_multiple_selection(self):
        enter_subform(self.driver, self.linklab_url)
        try:
            wait_and_find_element_by_xpath(self.driver, '//*[@id="caseTree"]/ul/li[2]/span[2]/span/div/div').click()
            wait_and_find_element_by_xpath(self.driver, '//*[@id="caseTree"]/ul/li[2]/ul/li[3]/span[2]/span/div/div').click()
            wait_and_find_elements_by_class_name(self.driver, 'replaceInput')[0].click()
            wait_and_find_elements_by_class_name(self.driver, 'replaceInput')[1].click()
            wait_and_find_elements_by_class_name(self.driver, 'replaceInput')[3].click()
            wait_and_find_elements_by_class_name(self.driver, 'replaceInput')[6].click()
            wait_and_find_elements_by_class_name(self.driver, 'replaceInput')[9].click()
            wait_and_find_elements_by_class_name(self.driver, 'modal-confirm')[1].click()
        except ValueError:
            print '多选题填写失败'
        commit_presence_by_xpath(self.driver, '多选题', '//*[@id="603746195224260608"]/div/div[4]/div/span/i[2]')

    # 文本题填写
    def test_write_text_question(self):
        enter_subform(self.driver, self.linklab_url)
        try:
            wait_and_find_element_by_xpath(self.driver, '//*[@id="caseTree"]/ul/li[2]/span[2]/span/div/div').click()
            wait_and_find_element_by_xpath(self.driver, '//*[@id="caseTree"]/ul/li[2]/ul/li[4]/span[2]').click()
            wait_and_find_elements_by_class_name(self.driver, 'addTestHalfOpen')[0].send_keys('test1')
            wait_and_find_elements_by_class_name(self.driver, 'opentext-input')[0].send_keys('test2')
            wait_and_find_elements_by_class_name(self.driver, 'opentext-input')[1].send_keys('test3')
            wait_and_find_elements_by_class_name(self.driver, 'modal-confirm')[1].click()
        except ValueError:
            print '文本题填写失败'
        commit_presence_by_xpath(self.driver, '文本题', '//*[@id="603748613970325504"]/div/div[4]/div/span/i[2]')

    # 数值题填写
    def test_write_number_question(self):
        enter_subform(self.driver, self.linklab_url)
        try:
            wait_and_find_element_by_xpath(self.driver, '//*[@id="caseTree"]/ul/li[2]/span[2]/span/div/div').click()
            wait_and_find_element_by_xpath(self.driver, '//*[@id="caseTree"]/ul/li[2]/ul/li[5]/span[2]/span/div/div').click()
            wait_and_find_elements_by_class_name(self.driver, 'replaceInput')[0].click()
            wait_and_find_elements_by_class_name(self.driver, 'opentext-input')[0].send_keys(123)
            wait_and_find_elements_by_class_name(self.driver, 'opentext-input')[2].send_keys(123)
            wait_and_find_elements_by_class_name(self.driver, 'modal-confirm')[1].click()
        except ValueError:
            print '数值题填写失败'
        commit_presence_by_xpath(self.driver, '数值题', '//*[@id="603750569803640832"]/div/div[4]/div/span/i[2]')

    # 填写时间题
    def test_write_time_question(self):
        enter_subform(self.driver, self.linklab_url)
        try:
            wait_and_find_element_by_xpath(self.driver, '//*[@id="caseTree"]/ul/li[2]/span[2]/span/div/div').click()
            wait_and_find_element_by_xpath(self.driver, '//*[@id="caseTree"]/ul/li[2]/ul/li[6]/span[2]/span/div/div').click()
            wait_and_find_elements_by_class_name(self.driver, 'time-set-input')[0].click()
            time.sleep(2)
            wait_and_find_elements_by_class_name(self.driver, 'date-now')[0].click()
            wait_and_find_elements_by_class_name(self.driver, 'modal-confirm')[0].click()
            wait_and_find_elements_by_class_name(self.driver, 'time-set-input')[1].click()
            time.sleep(2)
            wait_and_find_elements_by_class_name(self.driver, 'date-now')[-1].click()
            wait_and_find_elements_by_class_name(self.driver, 'modal-confirm')[0].click()
            wait_and_find_elements_by_class_name(self.driver, 'time-set-input')[3].click()
            time.sleep(2)
            wait_and_find_elements_by_class_name(self.driver, 'date-now')[-1].click()
            wait_and_find_elements_by_class_name(self.driver, 'modal-confirm')[1].click()
        except ValueError:
            print '时间题填写失败'
        commit_presence_by_xpath(self.driver, '时间题', '//*[@id="603750893989425152"]/div/div[4]/div/span/i[2]')

    # 2D表格内题填写
    def test_write_2D_question(self):
        enter_subform(self.driver, self.linklab_url)
        try:
            wait_and_find_element_by_xpath(self.driver, '//*[@id="caseTree"]/ul/li[2]/span[2]/span/div/div').click()
            wait_and_find_element_by_xpath(self.driver, '//*[@id="caseTree"]/ul/li[2]/ul/li[11]/span[2]/span/div/div').click()
            wait_and_find_elements_by_class_name(self.driver, 'replaceInput')[0].click()
            wait_and_find_elements_by_class_name(self.driver, 'removeChoice')[0].click()
            wait_and_find_elements_by_class_name(self.driver, 'replaceInput')[1].click()
            wait_and_find_elements_by_class_name(self.driver, 'replaceInput')[3].click()
            wait_and_find_elements_by_class_name(self.driver, 'replaceInput')[6].click()
            wait_and_find_elements_by_class_name(self.driver, 'replaceInput')[7].click()
            wait_and_find_elements_by_class_name(self.driver, 'replaceInput')[10].click()
            wait_and_find_elements_by_class_name(self.driver, 'replaceInput')[11].click()
            wait_and_find_element_by_xpath(self.driver, '//*[@id="603754121011785728"]/td[2]/div/a[2]').click()
            wait_and_find_element_by_xpath(self.driver, '//*[@id="603754166985551872"]/td[2]/div/a[3]').click()
            wait_and_find_elements_by_class_name(self.driver, 'modal-confirm')[1].click()

        except ValueError:
            print '2D题填写失败'
        commit_presence_by_xpath(self.driver, '2D问题', '//*[@id="603753652922904576"]/td[1]/div[1]/div[2]/span/i[2]')

    # 组内问题填写
    def test_group_question(self):
        enter_subform(self.driver, self.linklab_url)
        try:
            wait_and_find_element_by_xpath(self.driver, '//*[@id="caseTree"]/ul/li[2]/span[2]/span/div/div').click()
            wait_and_find_element_by_xpath(self.driver, '//*[@id="caseTree"]/ul/li[2]/ul/li[10]/span[2]/span/div/div').click()
            wait_and_find_elements_by_class_name(self.driver, 'selectText')[0].click()
            wait_and_find_elements_by_class_name(self.driver, 'selectText')[3].click()
            wait_and_find_elements_by_class_name(self.driver, 'selectText')[4].click()
            wait_and_find_elements_by_class_name(self.driver, 'opentext-input')[0].send_keys(u'你好')
            wait_and_find_elements_by_class_name(self.driver, 'opentext-input')[1].send_keys(123)
            wait_and_find_elements_by_class_name(self.driver, 'time-set-input')[0].click()
            time.sleep(1)
            wait_and_find_elements_by_class_name(self.driver, 'date-now')[0].click()
            wait_and_find_element_by_xpath(self.driver, '//*[@id="questionRight"]/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div/table/tbody/tr[2]/td[7]/div/div[3]/div[2]/ul/div/a[2]').click()
            wait_and_find_elements_by_class_name(self.driver, 'ant-cascader-input')[0].click()
            wait_and_find_element_by_xpath(self.driver, "//li[@title='北京市']").click()
            wait_and_find_element_by_xpath(self.driver, "//li[@title='北京辖区']").click()
            wait_and_find_element_by_xpath(self.driver, "//li[@title='昌平区']").click()
            wait_and_find_elements_by_class_name(self.driver, 'addGroupArea')[0].click()
            wait_and_find_elements_by_class_name(self.driver, 'selectText')[12].click()
            wait_and_find_elements_by_class_name(self.driver, 'selectText')[15].click()
            wait_and_find_elements_by_class_name(self.driver, 'modal-confirm')[1].click()
        except ValueError:
            print '组问题填写失败'
        commit_presence_by_xpath(self.driver, '组问题', '//*[@id="questionRight"]/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div/table/tbody/tr[2]/td[1]/div/div[2]/span/i[2]')

if __name__ == '__main__':
    unittest.main()









