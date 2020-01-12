# -*- encoding=utf8 -*-

__author__ = "jin"

from airtest.cli.runner import run_script
from airtest.cli.parser import runner_parser
import unittest
import datetime
from linklab_test_case.linklab_app.action.login import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
auto_setup(__file__)
dev = connect_device("Android://127.0.0.1:5037/emulator-5554")
poco = AndroidUiautomationPoco(dev)

class CreatSubject(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        start_app("com.linklab")

    def setUp(self):
        login(TEST_JYB_ONLINE)

    def test_creatsubject(self):
        poco(text="自动化测试").click()
        poco("com.linklab:id/project_add").click()
        poco("android:id/content").offspring("com.linklab:id/ll_root").offspring("com.linklab:id/ll_add_subject").child("android.widget.ImageView").click()
        poco(text="2").click()
        subject_name = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        poco("android.widget.EditText").click()
        text(subject_name)
        poco("提交").click()
        poco("android:id/content").child("android.widget.RelativeLayout").child(
            "android.widget.LinearLayout").offspring("com.linklab:id/project_grid_menu").child(
            "android.widget.LinearLayout")[3].child("com.linklab:id/menu_child_logo").click()
        try:
            if poco(text=subject_name).exists:
                print (subject_name)
                print ('新建案例成功')
            else:
                print('新建案例失败')
        except:
            print('新建案例失败')
        poco("com.linklab:id/head_back").click()

    def tearDown(self):
        loginoff()

    @classmethod
    def tearDownClass(cls):
        stop_app("com.linklab")


if __name__ == '__main__':
    ap = runner_parser()
    args = ap.parse_args()
    run_script(args, CreatSubject)