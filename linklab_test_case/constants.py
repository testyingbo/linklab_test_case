# coding=utf-8

import os.path

LINKLAB_HOOK_URL = 'https://oapi.dingtalk.com/robot/send?access_token=ba13ce40c2d761ebb241d2cdb8d3e1f7bd6bfb5f96bfff9e63eabd9ec6eec499'

"""用户名、密码配置"""
INNER_TEST = {
    'user_phone': '18819911006',
    'password': 'Ld.111'
}

INNER_ONLINE = {
    'user_phone': '16619939106',
    'password': '1234qwer'
}

YNTEST_ONLINE = {
    'user_phone': '18810068400',
    'password': 'ynwang1006'
}

DOCTOR_TEST = {
    'admin_user': 'linklab2',
    'password': 'admin'
}

TEST_JYB = {
    'user_phone': '18211143643',
    'password': '1234qwer'
}

TEST_JYB_ONLINE = {
    'user_phone': '18800009999',
    'password': '1234qwer'

}

JH_ONLINE = {
    'user_phone': '18511254593',
    'password': '1234qwer'
}

CRA_ONLINE = {
    'user_phone': '19999998888',
    'password': '1234qwer'
}

"""日志"""
RESULT_PATH = 'testresult'


"""测试地址"""
# test_offline
LOGIN_URL_TEST = 'http://192.168.1.115/usercenter/login'
BASE_URL_TEST = 'http://192.168.1.115'
BACKSTAGE_URL_TEST = 'http://192.168.1.115/backstage'
# test_online
BASE_URL_ONLINE = 'https://ecrf.linklab.com'
LOGIN_URL_ONLINE = 'https://ecrf.linklab.com/usercenter/login'
BACKSTAGE_URL_ONLINE = 'https://ecrf.linklab.com/backstage'
# test_master
BASE_URL_MASTER = 'https://linklab2-service.qa.linkdoc.com'
LOGIN_URL_MASTER = 'https://linklab2-service.qa.linkdoc.com/usercenter/login'
BACKSTAGE_URL = 'https://linklab2-service.qa.linkdoc.com/backstage'
# RC
RC_ONLINE = 'https://passport.linkdoc.com/'
RC_TEST = 'https://sb.linkdoc.com:9111/'


"""账号类型"""
TYPE_ADMIN = 1
TYPE_DOCTOR = 2

"""方法类型"""
METHOD_GET = 'GET'
METHOD_POST = 'POST'
METHOD_PUT = 'PUT'

file_path = "/Users/QA/PycharmProjects/linklab_test/1.png"


