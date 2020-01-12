#!/usr/bin/env python
# coding=utf8

import sys
import unittest
import os.path

from linklab_test_case.constants import *
from export_test import *
from linklab_data_report import *
from linklab_site_member import *
from linklab_test_case.action.send_mms_toding import *


if __name__ == "__main__":
    """构造测试类"""
    result_file = 'res.log'

    with open(result_file, 'w'):
        pass
    suite = unittest.TestSuite()
    suite.addTest(Linklab_Test("test_export"))
    suite.addTest(DatereportTest("test_get_core_number"))
    suite.addTest(DatereportTest("test_get_subject_form_number"))
    suite.addTest(SiteMemberTest("test_labnormal_download"))
    suite.addTest(SiteMemberTest("test_message_download"))
    suite.addTest(SiteMemberTest("test_download_station"))
    suite.addTest(SiteMemberTest("test_change_name"))
    suite.addTest(SiteMemberTest("test_invited_member"))
    suite.addTest(SiteMemberTest("test_delete_member"))

    """执行测试"""
    runner = unittest.TextTestRunner(failfast=False)
    runner.run(suite)