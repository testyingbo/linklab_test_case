# /usr/bin/python2
# -*- coding:utf-8 -*-

import json
import requests
import sys
import datetime
import time
from linklab_test_case.action.login import *
from linklab_test_case.constants import *
from linklab_test_case.linklab_api.web_api_list import *

reload(sys)
sys.setdefaultencoding('utf8')


def check_api_list(method, url_list, data):
    request_time_now = datetime.datetime.now()
    time.sleep(0.1)
    url = BASE_URL_ONLINE + url_list
    r = None
    success = True
    if not headers:
        raise Exception("Please Login first!")
    if method == 'GET':
        r = requests.get(url, headers=headers, verify=False)
    elif method == 'POST':
        r = requests.post(url, headers=headers, verify=False, data=data)
    elif method == 'PUT':
        r = requests.put(url, headers=headers, verify=False, data=data)
    if r.status_code != 200:
        success = False
    response_time_now = datetime.datetime.now()
    response_time = (response_time_now - request_time_now).microseconds
    body_json = None
    try:
        body_json = json.loads(r.text)
    except ValueError:
        print "URL {} Can not resolve response!".format(url)
        success = False
    if (not body_json) or body_json['status'] != 0:
        success = False
    if success:
        print 'URL `{}`, METHOD `{}`, STATUS:`{}`, TIME: `{}ms`'\
            .format(url, method, success, response_time/1000)
    else:
        print 'URL `{}`, METHOD `{}`, ERROR:`{}`, TIME: `{}ms`'\
            .format(url, method, body_json['errorMessage'], response_time/1000)



def get_all_apilist():
    apilist = []
    apilist.extend(message_center_api())
    apilist.extend(randomization_api())
    apilist.extend(management_others_api())
    apilist.extend(advanced_statistics_api())
    apilist.extend(data_repoter_api())
    apilist.extend(basic_interface_apis())
    apilist.extend(medical_coding())
    apilist.extend(timer_api())
    apilist.extend(check_invite_member())
    return apilist


def main():
    apilist = get_all_apilist()
    requests.packages.urllib3.disable_warnings()
    login_test(INNER_ONLINE['user_phone'], INNER_ONLINE['password'])

    print "API_LIST: {}".format(apilist)
    for entry in apilist:
        if len(entry) != 3:
            raise Exception("Invalid Arguments")
        success = check_api_list(entry[0], entry[1], entry[2])
    pass


if __name__ == '__main__':
    main()
