#!/usr/bin/env python
# coding=utf-8
import unittest
import json
import sys
import logging
reload(sys)

sys.setdefaultencoding('utf-8')

from linklab_test_case.constants import *
from linklab_test_case.action.login import *


class LinklabApiTest(unittest.TestCase):
    _driver = None

    def setUp(self):  # 设置初始化
        self.url_test = BASE_URL_TEST
        self.url_test_login = LOGIN_URL_TEST
        self.url_master = BASE_URL_MASTER
        self.url_master_login = LOGIN_URL_MASTER
        self.url_online = BASE_URL_ONLINE
        self.url_online_login = LOGIN_URL_ONLINE
        self.session_test = login_by_session_test(INNER_TEST['user_phone'], INNER_TEST['password'])
        self.session_master = login_by_session_test(INNER_TEST['user_phone'], INNER_ONLINE['password'])
        self.session_online = login_by_session_test(INNER_ONLINE['user_phone'], INNER_ONLINE['password'])


    def tearDown(self):
        pass

    def test_linklab_api(self):
        data = {
            "projectId": "547663432330317824",
            "currentRoleIsSite": "true",
            "siteId": -1,
            "mobile": "18500009999",
            "roleId": "547663432468729856"
        }
        self.diff_response('/management/project/projectRequestMember/', METHOD_POST, data)
        data = {
            "subjectId": "6439739798398701568",
            "title": "qw",
            "filter": [{"formId": "6435855955648319488",
                 "questionPdfVos": [{"questionId": "6435855963235815424"},
                                    {"questionId": "6435855963273564161"},
                                    {"questionId": "6438283453560524800"}]}],
        }
        self.diff_response('/management/exports/547663432330317824/subjectPdf', METHOD_POST, data)
        self.diff_response('/management/notifications/count?projectId=554150264150597632', METHOD_GET, None)
        self.diff_response('/management/proxy/survey/collecting/554150264150597632/dashboard/count?', METHOD_GET, None)

    def diff_response(self, url, method, data=None, data_special=None):
        if method == METHOD_GET:
            res_src = self.session_test.get(self.url_test + url, params=data)
            if data_special is None:
                res_master = self.session_test.get(self.url_master + url, params=data)
            else:
                res_master = self.session_test.get(self.url_master + url, params=data_special)
        elif method == METHOD_POST:
            res_src = self.session_test.post(self.url_test + url, data=data)
            if data_special is None:
                res_master = self.session_test.post(self.url_master + url, data=data)
            else:
                res_master = self.session_test.post(self.url_master + url, data=data_special)

        self.diff_result = True
        try:
            self.diff_text(json.loads(res_src.text)['data'], json.loads(res_master.text)['data'])
        except Exception as e:
            print e
            print res_src.text
            # print res_master.text
            return False
        if self.diff_result:
            return True
        else:
            print res_src.text
            # print res_master.text
            return False

    def diff_text(self, actual, expect):
        if type(actual) != type(expect):
            self.diff_result = False
        if isinstance(actual, list):
            for act, exp in zip(actual, expect):
                self.diff_text(act, exp)
        elif isinstance(actual, dict):
            a_minus_e = set(actual.keys()) - set(expect.keys())
            e_minus_a = set(expect.keys()) - set(actual.keys())
            a_and_e = set(actual.keys()) & set(expect.keys())
            if a_minus_e != set():
                for key in a_minus_e:
                    print 'new value remain: %s-%s' % (key, str(actual[key]))
                    self.diff_result = False
            elif e_minus_a != set():
                for key in e_minus_a:
                    print 'old value remain: %s-%s' % (key, str(expect[key]))
                    self.diff_result = False
            else:
                for key in a_and_e:
                    if type(actual) != type(expect):
                        print 'type not equal: key=%s, type_act=%s, type_exp=%s' % (key, type(actual[key]), type(expect[key]))
                        self.diff_result = False
                    elif isinstance(actual[key], list) or isinstance(actual[key], dict):
                        self.diff_text(actual[key], expect[key])
                    else:
                        if actual[key] != expect[key]:
                            print 'value not equal: key=%s, value_act=%s, value_exp=%s' % (key, str(actual[key]), str(expect[key]))
                            self.diff_result = False
        else:
            if actual != expect:
                print 'value not equal: act=%s, exp=%s' % (actual, expect)
                self.diff_result = False


if __name__ == "__main__":
    unittest.main()