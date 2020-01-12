#!/usr/bin/env python
# coding=utf-8
import unittest
from export_constants import *
from linklab_test_case.action.login import *
from linklab_test_case.action.web_service import *


class Linklab_Test(unittest.TestCase):
    _driver = None
    _linklab_url = ''

    def setUp(self):  # 设置初始化
        self._linklab_url = BASE_URL_ONLINE
        self._driver = webdriver.Chrome()
        self._driver.set_window_size(1920, 1080)
        self.session = login_by_session_test(JH_ONLINE['user_phone'], JH_ONLINE['password'])

    def tearDown(self):
        self._driver.quit()
        with open('labtest.log', 'a') as lab_file:
            lab_file.write(str(self._resultForDoCleanups) + '\n')

    def test_export(self):
        i= -1;  #为了引用数组而创建
        for response_url in response_urls:
            url = self._linklab_url + url_contains + response_url
            response = self.session.post(url)
            i=i+1
            try:
                res = json.loads(response.text)
                status = res['status']
                self.assertEqual(status, 0)
                print export_detasils[i]
            except ValueError:
                print 'export failed'


if __name__ == "__main__":
    unittest.main()
