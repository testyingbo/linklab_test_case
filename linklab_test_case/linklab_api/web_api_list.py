# /usr/bin/python2
# -*- coding:utf-8 -*-


import json
import sys


def check_invite_member():
    apis = []
    invite_member_web = ['POST', "/management/project/projectRequestMember",
                         {"projectId": "547663432330317824", "currentRoleIsSite": "true", "siteId": -1,
                          "mobile": "18500009999", "roleId": "547663432468729856"}]
    apis += [invite_member_web]
    return apis


def timer_api():
    apis = []
    project_pdf_export = ['POST', "/management/exports/547663432330317824/subjectPdf",
                          {"subjectId": "6439739798398701568", "title": "qw", "filter": [
                              {"formId": "6435855955648319488",
                               "questionPdfVos": [{"questionId": "6435855963235815424"},
                                                  {"questionId": "6435855963273564161"},
                                                  {"questionId": "6438283453560524800"}]}], }]  # 案例pdf导出
    apis += [project_pdf_export]
    return apis


def medical_coding():
    apis = []
    get_coding_nums = ['GET', "/management/proxy/survey/collecting/539599855290675200/coding/count",
                       json.dumps({"dictType": ""})]  # 获取编码数量
    apis += [get_coding_nums, ]
    return apis


def basic_interface_apis():
    apis = []
    # # sdv
    # subject_sdv_api = ['PUT', '/management/formController/subjectQuestion/sdv/{projectId}',
    #                    json.dumps({"projectId": "", "formId": "", "subjectId": "", "questionIds": ""})]
    # # 核查
    # subject_inspect_api = ['PUT', '/management/formController/subjectQuestion/check/{projectId}',
    #                        json.dumps({"projectId": "", "formId": "", "subjectId": "", "questionIds": ""})]
    # # 批量签名
    # subject_sign_batch_api = ['PUT', '/management/formController/subjectForm/sign/{projectId}',
    #                           json.dumps({"projectId": "", "password": "", "randCode": "", "subjectFormIds": ""})]
    # # 锁定
    # subject_lock_api = ['PUT', '/management/formController/subjectForm/lock/{projectId}',
    #                     json.dumps({"projectId": "", "subjectFormIds": ""})]
    # subject_remove_api = ['PUT', '/management/formBlackListController/remove/{projectId}',
    #                       json.dumps({"projectId": "", "id": ""})]
    # # 获取黑名单列表
    # get_back_list_api = ['GET', '/management/formBlackListController/formBlackList/{projectId}',
    #                      json.dumps({"projectId": "", "roleId": ""})]
    # # 添加黑名单
    # add_black_list_api = ['POST', ' /management/formBlackListController/pushAll/{projectId}',
    #                       json.dumps({"projectId": "",
    #                                   "formBlackLists": [[{"roleId": "123", "moduleId": "123", "moduleName": "模块1",
    #                                                        "formId": "6402412052165431296", "formName": "表单名称",
    #                                                        "deleted": "true"}]]})]
    # 获取案例列表接口
    get_subject_list_api = ['GET', '/management/notifications/count?projectId=554150264150597632', None]
    # dashboard 数量统计
    statistics_count_api = ['GET', '/management/proxy/survey/collecting/554150264150597632/dashboard/count?siteIds=',
                            None]
    # 标记数据安全监查、医学监查任务已完成表接口
    apis += [get_subject_list_api, statistics_count_api]
    return apis


def data_repoter_api():
    apis = []
    # 数据报告-核心指标
    report_corenumber_api = ['GET', '/management/reports/coreNumber/554150264150597632?projectId=554150264150597632',
                             None]
    # 数据报告-crf数据分析
    report_subject_api = ['GET', '/management/reports/subject/newly/554150264150597632?projectId=554150264150597632',
                          None]
    # 数据报告-质疑历史 siteIds 不传默认为当前用户拥有所有中心
    report_qc_statistics_api = ['GET',
                                '/management/reports/subject/totalNewly/554150264150597632?projectId=554150264150597632',
                                None]
    # 数据报告-案例总览
    report_subject_overview_api = ['GET',
                                   '/management/reports/subject/randomize/554150264150597632?projectId=554150264150597632',
                                   json.dumps({"projectId": "554150264150597632", "siteIds": ""})]
    # 数据报告-案例随机情况
    repoter_subject_randomize_api = ['GET',
                                     '/management/reports/qc/statistics/554150264150597632?projectId=554150264150597632&smooth=false',
                                     json.dumps({"projectId": "554150264150597632", "siteIds": ""})]
    # 数据报告-案例新增情况
    report_subject_newly_api = ['GET',
                                '/management/reports/subjectForm/554150264150597632?projectId=554150264150597632',
                                json.dumps({"projectId": "554150264150597632", "startDate": "", "endDate": ""})]
    apis += [report_corenumber_api, report_subject_api, report_qc_statistics_api, report_subject_overview_api,
             repoter_subject_randomize_api, report_subject_newly_api]
    return apis


def question_api():
    apis = []
    # 发起质疑
    qc_add_api = ['POST', '/management/qc/add/{projectId}',
                  json.dumps({"projectId": "", "subjectFormId": "", "title": "", "questionId": ""})]
    # 预发布质疑
    qc_pre_add_api = ['POST', '/management/preQc/add/{projectId}',
                      json.dumps({"projectId": "", "subjectFormId": "", "title": "", "questionId": ""})]
    # 回复质疑
    qc_reply_api = ['PUT', '/management/qc/reply/{projectId}',
                    json.dumps({"projectId": "", "message": "", "qcId": "", })]
    # 预发布回复质疑
    qc_pre_reply_api = ['PUT', '/management/preQc/reply/{projectId}',
                        json.dumps({"projectId": "", "message": "", "qcId": "", })]
    # 关闭质疑
    qc_close_api = ['PUT', '/management/qc/close/{projectId}', json.dumps({"projectId": "", "qcId": "", })]
    # 关于预发质疑
    qc_pre_close_api = ['PUT', '/management/preQc/close/{projectId}', json.dumps({"projectId": "", "qcId": "", })]
    # 查询质疑
    qc_search_api = ['POST', '/management/qc/listByType/{projectId}',
                     json.dumps({"projectId": "", "qcType": "", "sortDirection": "", "page": "1", "limit": "10", })]
    apis += [qc_add_api, qc_pre_add_api, qc_reply_api, qc_pre_reply_api, qc_close_api, qc_pre_close_api, qc_search_api]
    return apis


def advanced_statistics_api():
    apis = []
    # 查看统计历史
    get_statistics_histories_api = ['GET',
                                    '/management/project/554150264150597632/getStatisticsHistories?size=10&page=1',
                                    json.dumps({"offset": "0", "page": "10"})]
    # 不传 偏移量默认为0，分页容量默认为10
    apis += [get_statistics_histories_api]
    return apis


def usercenter_api_list():
    apis = []
    # 短信验证码登录
    send_phone_code_api = ['POST', "/usercenter/sendPhoneCodeForLogin",
                           json.dumps({"validateCode": "1234", "phone": '18810068400'})]
    ['POST', "/usercenter/login", json.dumps({"validateCode": "1234", "username": "18810068400", "loginMode": ''})]
    # App
    send_reset_code_api = ['POST', '/usercenter/sendResetPwdCode',
                           json.dumps({"username": '18810068400', "validateCode": "1234"})]
    # 找回密码接口
    # app 用户认证
    modify_info_api = ['POST', '/usercenter/modifyinfo', json.dumps(
        {"city": "北京", "province": "", "institution": "", "postTitle": "", "department": "", "isAuth": "1",
         "authImage": "", "acquaintId": "", "avatar": "", "realName": ""})]
    get_project_api = ['POST', '/usercenter/getProjects', json.dumps({'pageNopageNo': '1', "pageSize": '10'})]
    apis += [send_phone_code_api, send_reset_code_api, modify_info_api, get_project_api]
    return apis


def management_others_api():
    apis = []
    # 获取受试者图片列表
    get_subject_image_api = ['GET', '/management/image/subject',
                             {"subject_id": "6442633542236123136", "visit_id": "554150264339341312"}]
    # 获取案例下模块列表
    get_cycle_modules_api = ['GET', '/management/proxy/survey/collecting/6442937077330886656/getCycleModules',
                             {"siteId": "", "subjectStatus": "", "sn": "", "page": "1", "limit": "10",
                              "subjectId": "6442937077330886656",
                              "moduleId": "554150264339341313"}]
    # 获取模块下的表单接口
    get_module_form_api = ['GET', '/management/proxy/survey/collecting/6442937077330886656/getModule',
                           {"subjectId": "6442937077330886656", "moduleId": "554150264339341313"}]
    apis += [get_subject_image_api, get_cycle_modules_api, get_module_form_api]
    return apis


def message_center_api():
    apis = []
    get_noread_notification_count = ['GET', "/management/notifications/count",
                                     {"source": "", "projectId": ""}]  # 获取通知未读数量接口
    message_as_read = ['PUT', "/management/notifications/read", json.dumps({"id": ""})]  # 将消息置为已读
    get_message_list = ['GET', "/management/notifications/", json.dumps(
        {"source": "", "projectId": "", "page": "1", "limit": "", "types": "sn", "read": 0})]  # 获取消息列表接口
    message_read_all = ['PUT', "/management/notifications/readAll",
                        json.dumps({"source": "", "projectId": "", "types": "sn"})]  # 标记全部已读
    apis += [get_noread_notification_count, message_as_read, get_message_list, message_read_all]
    return apis


def randomization_api():
    apis = []
    # add_random_config_api = ['POST', " /management/random/addRandomConfig", json.dumps(
    #     {"source": "", "randType": "", "randNum": "", "sourceId": "", "blindType": "", "groups": "",
    #      "randNumRuleType": "", "randNumRules": "", "factors": "", "factorDetails": "", })]
    # change_random_config_api = ['POST', "management/random/updateRandomConfig/{configId}", json.dumps(
    #     {"factors": "", "factorDetails": "", "randType": "", "randNum": "", "randNumRuleType": "", "randNumRules": "",
    #      "groups": "", })]
    # submit_random_config_api = ['POST', "management/random/submitRandomConfig/{configId}", None]
    get_random_config_api = ['GET', "/management/random/getRandomConfigInfo?sourceId=554150264150597632",
                             json.dumps({"sourceId": ""})]
    get_random_number_api = ['POST', "/management/random/getRandomNumber",
                             json.dumps({"sourceId": "554150264150597632", "factors": [],
                                         "instanceId": "6442937077330886656", })]
    apis += [get_random_config_api,
             get_random_number_api]
    return apis



