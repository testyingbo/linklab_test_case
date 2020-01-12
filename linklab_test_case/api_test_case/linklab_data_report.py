# /usr/bin/python2
# -*- coding:utf-8 -*-
# 数据报告测试用例
import json
import time
from selenium import webdriver
import unittest
from linklab_test_case.constants import *
import linklab_test_case.action.login as login


class DatereportTest(unittest.TestCase):
    driver = None
    linklab_url = ''

    def setUp(self):
        self.project_id = '522142540358426624'
        self.driver = webdriver.Chrome()
        self.linklab_url = BASE_URL_ONLINE
        self.session = login.login_by_session_test(TEST_JYB_ONLINE['user_phone'], TEST_JYB_ONLINE['password'])

    def tearDown(self):
        self.driver.quit()
        with open('labtest.log', 'a') as lab_file:
            lab_file.write(str(self._resultForDoCleanups) + '\n')

    def test_get_core_number(self):
        url = self.linklab_url + '/management/reports/coreNumber/' + self.project_id
        data = {
            'projectId': self.project_id
        }
        response = self.session.get(url, params=data)

        try:
            res = json.loads(response.text)['data']
            self.assertEqual(res['checkForm'], 20)
            self.assertEqual(res['qcTotal'], 22)
            self.assertEqual(res['total'], 67)
            self.assertEqual(res['signForm'], 1)
            self.assertEqual(res['submitForm'], 135)
            print '数据数量正确'
        except ValueError:
            print '数据数量不正确'

    def test_get_subject_form_number(self):

        url = self.linklab_url + '/management/reports/subjectForm/' + self.project_id
        data = {
            'projectId': self.project_id
        }
        response = self.session.get(url, params=data)
        res = json.loads(response.text)['data']
        sum_ret = {
            "sumSt-1": 0, "sumSt0": 0, "sumSt1": 0, "sumSt2": 0,
            "sumSt3": 0, "sumSt4": 0, "sumSt5": 0, "sumSt6": 0, "sumSt9": 0
        }
        for i in res:
            if i['count'] is None:
                continue
            count = i['count']
            sum_ret["sumSt" + str(i['status'])] += count
        try:
            self.assertEqual(sum_ret['sumSt0'], 716)
            self.assertEqual(sum_ret['sumSt1'], 155)
            self.assertEqual(sum_ret['sumSt2'], 154)
            self.assertEqual(sum_ret['sumSt3'], 19)
            self.assertEqual(sum_ret['sumSt4'], 19)
            self.assertEqual(sum_ret['sumSt5'], 19)
            self.assertEqual(sum_ret['sumSt6'], 18)
            self.assertEqual(sum_ret['sumSt9'], 1)
            print '表单数量正确'
        except ValueError:
            print '表单数量不一致'


if __name__ == '__main__':
    unittest.main()







