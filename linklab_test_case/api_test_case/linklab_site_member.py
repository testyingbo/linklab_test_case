# -*- coding:utf8 -*-
import datetime
import unittest
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import json
from selenium import webdriver
from linklab_test_case.constants import *
from linklab_test_case.action.login import *


class SiteMemberTest(unittest.TestCase):
    def setUp(self):
        self.project_id = '599345115635499008'
        self.project_site_id = '599376385392361472'
        self.driver = webdriver.Chrome()
        self.linklab_url = BASE_URL_ONLINE
        self.session = login_by_session_test(TEST_JYB_ONLINE['user_phone'], TEST_JYB_ONLINE['password'])

    def tearDown(self):
        self.driver.quit()
        # with open('labtest.log', 'a') as labfile:
        # labfile.write(str(self._resultForDoCleanups)+'\n')

    # 新建分中心测试用例接口测试
    def test_creat_site(self):
        url = self.linklab_url + '/management/permission/projectSite/' + self.project_id
        site_name = datetime.datetime.now().strftime('%H%M%S')
        header = {'Content-Type': "application/json"}
        data = "{\"projectId\":\""+self.project_id+"\",\"projectSites\":[{\"siteName\":\""+site_name+"\",\"siteCode\":\""+site_name+"\"}]}"
        print data
        response = self.session.post(url=url, data=data, headers=header)
        print response.text
        res = json.loads(response.text)['data']
        site_name_list = []
        for site in res:
            i = site['siteName']
            site_name_list.append(i)
        try:
            self.assertIn(site_name, site_name_list)
            print '新建分中心成功'
        except ValueError:
            print '新建分中心失败'

    # 新建下载分中心正常值任务
    def test_labnormal_download(self):
        url_labnormal = self.linklab_url + '/management/exports/' + self.project_id + '/siteProperties'
        data_labnormal = {
            'projectId': self.project_id,
            'type': 44
        }
        response_labnormal = self.session.post(url_labnormal, params=data_labnormal)
        res_labnormal = json.loads(response_labnormal.text)['data']
        try:
            self.assertEqual(res_labnormal['statues'], '0')
            self.assertEqual(res_labnormal['type'], '44')
            print '新建分中心正常值下载任务成功'
        except ValueError:
            print '新建分中心正常值下载任务失败'

    # 新建下载信息任务用例
    def test_message_download(self):
        url_message = self.linklab_url + '/management/exports/' + self.project_id + '/siteUsers'
        data_message = {
            'projectId': self.project_id,
            'type': 43
        }
        response_message = self.session.post(url_message, params=data_message)
        res_message = json.loads(response_message.text)['data']
        try:
            self.assertEqual(res_message['statues'], '0')
            self.assertEqual(res_message['type'], '43')
            print '新建信息下载任务成功'
        except ValueError:
            print '新建信息下载任务失败'

    # 下载站下载信息和分中心正常值任务失败成功校验用例
    def test_download_station(self):
        url = self.linklab_url + '/management/exports/' + self.project_id
        data = {
            'projectId': self.project_id
        }
        response = self.session.get(url, params=data)
        try:
            res = json.loads(response.text)['data']
            data_labnomal = res[-2]
            data_message = res[-1]
            self.assertEqual(data_labnomal['statues'], '1')
            self.assertEqual(data_labnomal['type'], '44')
            self.assertEqual(data_message['statues'], '1')
            self.assertEqual(data_message['type'], '43')
            print '下载站下载任务成功'
        except ValueError:
            print '下载站下载任务失败'

    # 修改分中心名称测试用例
    def test_change_name(self):
        url = self.linklab_url+"/management/permission/updateProjectSiteName/"+self.project_id+"/"+self.project_site_id
        new_site_name = datetime.datetime.now().strftime('%H%M%S')
        data = "{siteName: \""+new_site_name+"\", siteCode: \""+new_site_name+"\", freeze: false}"
        header = {'Content-Type': "application/json"}
        response = self.session.post(url=url, data=data, headers=header)
        try:
            res = json.loads(response.text)['data']
            new_res = res['siteName'].encode('unicode-escape').decode('string_escape')
            self.assertEqual(new_res, new_site_name)
            print '修改分中心名称成功'
        except ValueError:
            print '修改分中心名称失败'

    # 邀请成员进入全部分中心
    def test_invited_member(self):
        url = self.linklab_url + '/management/project/batchInviteMembers/' + self.project_id
        data = {
            'roleIds': '599345115656470528',
            'mobileOrEmails': '18211143643',
            'usernames': '贾英博',
            'siteIds': '-1'
        }
        response = self.session.post(url, params=data)
        res = json.loads(response.text)['data']
        try:
            self.assertEqual(res, 'OK')
            print '邀请成员进入全部分中心成功'
        except ValueError:
            print '邀请成员进入全部分中心失败'

    # 删除上一次邀请进入全部分中心的成员
    def test_delete_member(self):
        url = self.linklab_url + '/management/permission/deleteProjectMember'
        data = {
            'projectId': self.project_id,
            'userId': '509460419408744448',
            'id': '602230811818037248',
            'projectName': '功能测试',
            'userName': '贾英博'
        }
        response = self.session.post(url, params=data)
        res = json.loads(response.text)['status']
        try:
            self.assertEqual(res, 0)
            print '删除成员成功'
        except ValueError:
            print '删除成员失败'


if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(SiteMemberTest)
    suite = unittest.TestSuite([suite1])
    unittest.TextTestRunner(verbosity=2).run(suite)