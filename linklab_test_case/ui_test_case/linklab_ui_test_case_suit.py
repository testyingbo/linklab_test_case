#!/usr/bin/env python
# coding=utf8

import sys
import unittest
import os.path

from linklab_test_case.constants import *
from linklab_single_choice import *
from linklab_creat_subject import *
from linklab_write_expression import *
from linlab_alterdata_question import *
from linklab_test_case.action.send_mms_toding import *


if __name__ == "__main__":
    """构造测试类"""
    result_file = 'res.log'

    with open(result_file, 'w'):
        pass
    suite = unittest.TestSuite()
    suite.addTest(CreatSubject("test_creat_subject"))
    suite.addTest(LinklabTest("test_single_choice"))
    suite.addTest(LinklabTest("test_all_subject"))
    suite.addTest(LinklabTest("test_load_file"))
    suite.addTest(LinklabTest("test_grade"))
    suite.addTest(LinklabTest("test_address"))
    suite.addTest(CreatSubject('test_write_multiple_selection'))
    suite.addTest(CreatSubject('test_write_text_question'))
    suite.addTest(CreatSubject('test_write_number_question'))
    suite.addTest(CreatSubject('test_write_time_question'))
    suite.addTest(CreatSubject('test_write_2D_question'))
    suite.addTest(CreatSubject('test_group_question'))
    suite.addTest(WriteExpression('test_write_ifresult'))
    suite.addTest(WriteExpression('test_write_answerCheck'))
    suite.addTest(WriteExpression('test_write_timeExpression'))
    suite.addTest(WriteExpression('test_write_math_value'))
    suite.addTest(WriteExpression('test_write_containsAny'))
    suite.addTest(WriteExpression('test_write_notify'))
    suite.addTest(WriteExpression('test_freezeForm'))
    suite.addTest(WriteExpression('test_write_siteProperty_normal'))
    suite.addTest(WriteExpression('test_write_parseRegxp'))
    suite.addTest(WriteExpression('test_write_parseInt'))
    suite.addTest(WriteExpression('test_write_now'))
    suite.addTest(WriteExpression('test_write_voiid'))
    suite.addTest(WriteExpression('test_write_numberGenerator'))
    suite.addTest(WriteExpression('test_write_sae'))
    suite.addTest(AlterData('test_alter_data'))
    suite.addTest(AlterData('test_alter_group_data'))
    suite.addTest(AlterData('test_make_question'))
    suite.addTest(AlterData('test_close_question'))
    """执行测试"""
    runner = unittest.TextTestRunner(failfast=False)
    runner.run(suite)

