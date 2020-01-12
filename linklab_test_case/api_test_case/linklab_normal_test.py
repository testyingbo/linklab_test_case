#!/usr/bin/env python
# coding=utf-8
import unittest
import os
import datetime
import random
from linklab_test_case.action.login import *
from linklab_test_case.action.web_service import *


class Linklab_Test(unittest.TestCase):
    _driver = None
    _linklab_url = ''

    def setUp(self):  # 设置初始化
        self._linklab_url = BASE_URL_ONLINE
        self._driver = webdriver.Chrome()
        self._driver.set_window_size(1920, 1080)
        login(self._driver, self._linklab_url, INNER_ONLINE)
        self.session = login_by_session_test(YNTEST_ONLINE['user_phone'], YNTEST_ONLINE['password'])

    def tearDown(self):
        self._driver.quit()
        with open('labtest.log', 'a') as lab_file:
            lab_file.write(str(self._resultForDoCleanups) + '\n')

    def test_get_project_num(self):
        url = self._linklab_url + '/management/project/getProjects'
        data = {
            'pageNo': 1,
            'pageSize': 10000,
        }
        response = self.session.post(url, params=data)
        try:
            res = json.loads(response.text)
            print res
            amount = res['data']
            projectcount = len(amount)
            print projectcount
            for i in range(projectcount):
                project_id = res['data'][i]['id']
                f = open('project_id_list.txt', 'w')
                f.write(str(project_id) + "\n")
                if os.path.getsize('project_id_list.txt') > 0:
                    pass
                else:
                    print 'error'
        except ValueError:
            print 'Error 2'

    def test_goto_project(self):
        self._driver.get(self._linklab_url + "/project/user/#/")
        time.sleep(1)
        wait_and_find_elements_by_link_text(self._driver, "进入项目")[1].click()
        time.sleep(2)
        file_name = '项目' + datetime.datetime.now().strftime('%H%M%S') + '.png'
        self._driver.save_screenshot(file_name)
        wait_and_find_elements_by_class_name(self._driver, "navItem-name")[2].click()
        wait_and_find_element_by_xpath(self._driver, "//*[@id='root']/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/a[1]/span[2]").click()
        wait_and_find_element_by_class_name(self._driver, 'ant-select-selection__placeholder').click()
        wait_and_find_elements_by_class_name(self._driver, 'ant-select-dropdown-menu-item')[0].click()
        wait_and_find_element_by_xpath(self._driver, '/html/body/div[2]/div/div[2]/div/div[1]/div[3]/div/button[2]').click()
        time.sleep(3)
        file_name = '案例编号表' + datetime.datetime.now().strftime('%H%M%S') + '.png'
        self._driver.save_screenshot(file_name)
        time_identifier = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        case_number = 'test' + time_identifier
        print case_number
        wait_and_find_elements_by_xpath(self._driver, "form-control opentext-input")[0].send_keys(case_number)
        wait_and_find_elements_by_xpath(self._driver, "form-control opentext-input")[1].send_keys(case_number)
        test_age = random.randint(20, 100)
        wait_and_find_elements_by_xpath(self._driver, "form-control opentext-input")[2].send_keys(test_age)


if __name__ == "__main__":
    unittest.main()
