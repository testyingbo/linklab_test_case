# coding=utf-8
import requests
import json


def send_result_to_ding(url, build_name, result):
    header = {
        'Content-Type': 'application/json'
    }
    if result == 'pass':
        data = {
            "msgtype": "text",
            "text": {
                "content": build_name + "测试通过"
            },
        }
    elif result == 'fail':
        data = {
            "msgtype": "text",
            "text": {
                "content": build_name + "测试失败"
            },
        }
    else:
        data = {
            "msgtype": "text",
            "text": {
                "content": build_name + result
            },
        }
    response = requests.post(url, data=json.dumps(data), headers=header)
    print response.text