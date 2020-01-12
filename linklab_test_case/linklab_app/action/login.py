# -*- encoding=utf8 -*-
__author__ = "jin"

from airtest.core.api import *
from linklab_test_case.linklab_app.constants import *

auto_setup(__file__)
dev = connect_device("Android://127.0.0.1:5037/emulator-5554")
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(dev)

def login(user):
    poco("com.linklab:id/tv_login").click()
    poco("com.linklab:id/login_et_account").click()
    poco("com.linklab:id/login_img_clearAccount").click()
    text(user['user_phone'])
    poco("com.linklab:id/login_et_pwd").click()
    text(user['password'])
    poco("com.linklab:id/login_tv_commit").click()
    poco("com.linklab:id/head_cancel").click()


def loginoff():
    poco("com.linklab:id/tab_iv_mine").click()
    poco(text="账号与安全").click()
    poco("com.linklab:id/setting_tv_exit").click()
    poco("com.linklab:id/btn_pos").click()

