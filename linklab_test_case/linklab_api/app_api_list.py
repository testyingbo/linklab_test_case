# /usr/bin/python2
# -*- coding:utf-8 -*-

import json
import requests
import sys
import datetime
import time
from linklab_test_case.action.login import *
from linklab_test_case.constants import *


def app_funcation_api_list():
    apis = []
    get_image_api = ['GET', "/usercenter/getAppCaptcha", json.dumps({"randomCode": "", "hl ": ""})]  # 获取图片验证码
    client_update_api = ['GET', "/management/general/upgrade",
                         json.dumps({"device_type": "", "device_type": ""})]  # 客户端升级信息
    get_upload_token = ['POST', "/management/qiniu/uploadToken", json.dumps({"stype": "", "hl ": ""})]  # 获取上传图片token
    send_reset_pwd_code = ['POST', "/usercenter/sendResetPwdCode", json.dumps(
        {"username": "", "validateCode": "", "randomCode": "", "hl ": "", "source": "", })]  # 发送找回密码短信
    submit_pwd_config = ['POST', "/usercenter/resetpwd", json.dumps(
        {"validCode": "", "username": "", "newPassword ": "", "newPasswordConfirm": "", "hl ": "", })]  # 提交修改密码配置
    change_pwd_api = ['POST', "/usercenter/changepwd", json.dumps(
        {"oldPassword": "", "newPassword": "", "newPasswordConfirm": "", "hl": "", })]  # 修改密码接口
    get_user_info = ['GET', "/usercenter/userInfo", json.dumps({"source": "", "hl": ""})]  # 获取个人信息
    get_centers_list = ['GET', "/management/permission/getSitesForView",
                        json.dumps({"projectId": "", "source": ""})]  # 获取分中心接口
    add_center_api = ['POST', "/management/permission/projectSite/{projectId}",
                      json.dumps({"pid": "", "siteName": "", "hl": "", "hl ": "", })]  # 添加分中心
    update_center_api = ['POST', "/management/permission/updateProjectSiteName/{siteId}",
                         json.dumps(
                             {"projectSiteId": "", "siteName": "", "projectId": "", "hl ": "", "source": ""})]  # 更新分中心

    get_project_role = ['GET', "/management/permission/projectRole",
                        json.dumps({"projectId": "", "source": "", "hl ": "", })]
    get_subject_form = ['GET', "/management/proxy/survey/collecting/{projectId}/{subjectId}/subjectForms ",
                        json.dumps({"source": "", "hl ": "", })]  # 获取模块结构
    add_follow_api = ['POST', "/management/proxy/survey/collecting/addFollow", json.dumps(
        {"source": "", "subjectId": "", "projectId": "", "moduleId": "", "hl": "", })]  # 新增随访模块
    move_member_api = ['POST', "/management/permission/moveMember", json.dumps(
        {"source": "", "hl": "", "projectId": "", "userId": "", "targetSiteId": "", })]  # 成员移动
    exit_member_api = ['POST', "/management/project/exitUserProject",
                       json.dumps({"source": "", "hl": "", "projectId": "", "userId": ""})]  # 成员退出
    delete_member_api = ['POST', "/management/permission/deleteProjectMember", json.dumps(
        {"source": "", "hl": "", "projectId": "", "userId": "", "id ": "", "projectName": "",
         "userName ": ""})]  # 删除成员
    project_site_member_list = ['GET', "/management/permission/projectSiteMemberList/{projectId}",
                                json.dumps({"source": "", "hl": ""})]  # 项目成员所属中心
    get_suject_modules = ['GET', "/management/proxy/survey/collecting/{projectId}/subjectModules", json.dumps(
        {"source": "", "hl": "", "siteId": "", "subjectStatus": "", "sn": "", "page": "", "limit": ""})]  # 获取案例列表
    get_all_project_role = ['GET', "/management/permissionRole/getAllRoleByProject/{projectId}",
                            json.dumps({"source": "", "hl": ""})]  # 获取项目内所有角色
    get_provice_city = ['GET', "/usercenter/data/provinceCity", None]  # 获取省市层级关系
    get_invite_role_project = ['GET', "/management/permissionRole/getInviteRoleByProject/{projectId}",
                               json.dumps({"source": "", "hl": ""})]  # 获取项目内所有角色
    get_provice_city_organization = ['GET', "/usercenter/data/province/city/institutions",
                                     json.dumps({"provinceName": "", "cityName": ""})]  # 获取省市城市下的机构列表
    get_proveice_city_academy = ['GET', "/usercenter/data/province/city/academys",
                                 json.dumps({"provinceName": "", "cityName": ""})]  # 获取省市下的院校

    apis += [get_invite_role_project, get_provice_city, get_all_project_role, get_suject_modules,
             project_site_member_list, delete_member_api, exit_member_api, move_member_api, add_follow_api,
             get_subject_form, get_project_role, update_center_api, add_center_api, get_centers_list, get_user_info,
             change_pwd_api, submit_pwd_config, send_reset_pwd_code, get_upload_token, client_update_api, get_image_api,
             get_provice_city_organization, get_proveice_city_academy]

    return apis


def app_user_register():
    apis = []
    app_user_login_api = ['POST', "/usercenter/login",
        {"username": "18500540733", "password": "liutao123", "source": "", "randomCode": "", "validateCode": "", "device_id": "",
         "device_type": "", "app_version": "", "system": "", "hl ": "", }]  # app登录接口
    app_user_sendregistercode = ['POST', "/usercenter/sendRegisterCode",
                                 json.dumps({"mobile": "", "source": "", "hl": "", })]  # app注册发送短信验证码
    app_user_register_api = ['POST', "/usercenter/registerApp", json.dumps(
        {"mobile": "", "nickName": "", "password": "", "vaildCode": "", "uuid": "", "source": "",
         "hl ": "", })]  # app注册提交接口
    apis += [app_user_login_api, app_user_sendregistercode, app_user_register_api]
    return apis


def app_api_new():
    apis = []

    get_user_desc = ['GET', "/usercenter/userDesc", json.dumps({"id": ""})]  # 关联信息接口

    get_random_info_api = ['GET', "management/random/getSubjectRandomInfo", json.dumps({"instanceId": ""})]  # 受试者随机信息
    update_user_name_api = ['POST', "/usercenter/updUserRealName", json.dumps({"realName": ""})]  # 追加真实姓名
    project_member_list = ['GET', "/management/permission/projectMemberList/{projectId}/{userId}", None]  # 用户在权限内的角色名称
    get_task_count = ['GET', "management/task/countByClass/{projectId}", json.dumps({"projectId": ""})]  # 任务中心获取任务数量
    get_task_info = ['GET', "/management/task/filterTasks/{projectId}", json.dumps(
        {"page": "", "limit": "", "typeId": "", "order": "", "queryType": "", "keyword": "", })]  # 获取任务详情
    batch_statu_stask = ['POST', "/management/proxy/survey/collecting/${projectId}/subjectForm/batchStatusTask",
                         json.dumps(
                             {"auditStatus": "", "paramObjectList": "", "password": "", "password ": ""})]  # 批量签名和锁定
    get_linklab_customer = ['GET', "management/project/linklabInfo", None]  # 获取客服信息
    freeze_or_unfreeze_api = ['PUT', "/management/proxy/survey/collecting/{projectId}/subject/freeze",
                              json.dumps({"subjectId": ""})]  # 冻结解冻案例接口
    lock_menu_api = ['PUT', "/management/proxy/survey/collecting/{projectId}/subjectForm/changeStatus/lock",
                     json.dumps({"siteId": "", "subjectFormId": ""})]  # 锁定表单接口
    unlock_menu_api = ['PUT', "/management/proxy/survey/collecting/{projectId}/subjectForm/unlock",
                       json.dumps({"siteId": "", "subjectFormId": ""})]  # 解锁表单接口
    menu_sign_api = ['PUT', "/management/proxy/survey/collecting/{projectId}/subjectForm/changeStatus/sign",
                     json.dumps({"siteId": "", "subjectFormId": "", "password": "", "randCode": ""})]  # 表单签名接口
    get_avatar_url = ['GET', "management/qiniu/getAvatarUrl", json.dumps({"userId": ""})]  # 获取用户头像

    apis += [get_user_desc, get_random_info_api, update_user_name_api, project_member_list, get_task_count,
             get_task_info, batch_statu_stask, get_linklab_customer, freeze_or_unfreeze_api, lock_menu_api,
             unlock_menu_api, menu_sign_api, get_avatar_url]
    return apis

