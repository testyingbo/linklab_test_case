#!/usr/bin/env python
# coding=utf8

import sys
import unittest
import os.path

from linklab_zhuliucheng_detail import *


# 串行
def serial():
    suite = unittest.TestSuite()
    suite.addTest(Serialtest("test_creat_subject"))
    suite.addTest(Serialtest("test_submit"))
    suite.addTest(Serialtest("test_SDV"))
    suite.addTest(Serialtest("test_checked"))
    suite.addTest(Serialtest("test_sign"))
    suite.addTest(Serialtest("test_lock"))
    runner = unittest.TextTestRunner(failfast=False)
    runner.run(suite)


# 并行
def parallel():
    suite = unittest.TestSuite()
    suite.addTest(ParallelTest("test_creat_subject"))
    suite.addTest(ParallelTest("test_submit"))
    suite.addTest(ParallelTest("test_checked"))
    suite.addTest(ParallelTest("test_SDV"))
    suite.addTest(ParallelTest("test_sign"))
    suite.addTest(ParallelTest("test_lock"))
    runner = unittest.TextTestRunner(failfast=False)
    runner.run(suite)


# 无SDV无签名
def nosdv():
    suite = unittest.TestSuite()
    suite.addTest(Nosdvtest("test_creat_subject"))
    suite.addTest(Nosdvtest("test_submit"))
    suite.addTest(Nosdvtest("test_checked"))
    suite.addTest(Nosdvtest("test_lock"))
    runner = unittest.TextTestRunner(failfast=False)
    runner.run(suite)


if __name__ == "__main__":
    """构造测试类"""
    serial()
    parallel()
    nosdv()

