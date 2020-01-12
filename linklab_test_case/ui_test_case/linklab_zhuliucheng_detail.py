#!/usr/bin/env python
# coding=utf-8
import unittest
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from linklab_test_case.ui_test_case.linklab_zhuliucheng_common import *

serial_position = 3
parallel_position = 1
serial_sdv_position = 1
parallel_sdv_position = 0
nosdv_position = 0
serial_url = "https://ecrf.linklab.com/management/task/countByClass/583447510010155008?projectId=583447510010155008"
parallel_url = "https://ecrf.linklab.com/management/task/countByClass/646441347114954752?projectId=646441347114954752"
nosdv_url = "https://ecrf.linklab.com/management/task/countByClass/646441774650732544?projectId=646441774650732544"


class Serialtest(unittest.TestCase):
    _driver = None
    _linklab_url = ''

    def setUp(self):  # 设置初始化
        self._linklab_url = BASE_URL_ONLINE
        self._driver = webdriver.Chrome()

    def tearDown(self):
        self._driver.quit()
        with open('labtest.log', 'a') as lab_file:
            lab_file.write(str(self._resultForDoCleanups) + '\n')

    def test_creat_subject(self):
        position = serial_position
        creat_subject(self, position)

    def test_submit(self):
        position = serial_position
        submit(self, position)

    def test_SDV(self):
        position = serial_sdv_position
        url = serial_url
        SDV(self, position, url)

    def test_checked(self):
        position = serial_position
        url = serial_url
        checked(self, position, url)

    def test_sign(self):
        position = serial_position
        url = serial_url
        sign(self, position, url)

    def test_lock(self):
        position = serial_position
        url = serial_url
        lock(self, position, url)


class ParallelTest(unittest.TestCase):
    _driver = None
    _linklab_url = ''

    def setUp(self):  # 设置初始化
        self._linklab_url = BASE_URL_ONLINE
        self._driver = webdriver.Chrome()

    def tearDown(self):
        self._driver.quit()
        with open('labtest.log', 'a') as lab_file:
            lab_file.write(str(self._resultForDoCleanups) + '\n')

    def test_creat_subject(self):
        position = parallel_position
        creat_subject(self, position)

    def test_submit(self):
        position = parallel_position
        submit(self, position)

    def test_SDV(self):
        position = parallel_sdv_position
        url = parallel_url
        SDV(self, position, url)

    def test_checked(self):
        position = parallel_position
        url = parallel_url
        checked(self, position, url)

    def test_sign(self):
        position = parallel_position
        url = parallel_url
        sign(self, position, url)

    def test_lock(self):
        position = parallel_position
        url = parallel_url
        lock(self, position, url)


class Nosdvtest(unittest.TestCase):
    _driver = None
    _linklab_url = ''

    def setUp(self):  # 设置初始化
        self._linklab_url = BASE_URL_ONLINE
        self._driver = webdriver.Chrome()

    def tearDown(self):
        self._driver.quit()
        with open('labtest.log', 'a') as lab_file:
            lab_file.write(str(self._resultForDoCleanups) + '\n')

    def test_creat_subject(self):
        position = nosdv_position
        creat_subject(self, position )

    def test_submit(self):
        position = nosdv_position
        submit(self, position)

    def test_checked(self):
        position = nosdv_position
        url = nosdv_url
        checked(self, position, url)

    def test_lock(self):
        position = nosdv_position
        url = nosdv_url
        lock(self, position, url)