# --*-- coding:utf8 --*--
# 修改按钮是否存在来判断表单是否提交成功
import time
from  linklab_test_case.common.enter_subform import *

# 该方法用来确认元素是否存在，如果存在返回flag=true，否则返回false
def is_commit_presence_by_xpath(driver, element):
    flag = True
    try:
        driver.find_element_by_xpath(element)
        return flag
    except ValueError:
        flag = False
        return flag


# element为任一修改按钮的xpath
def commit_presence_by_xpath(driver, case_name, element):
    time.sleep(3)
    driver.refresh()
    time.sleep(3)
    try:
        if is_commit_presence_by_xpath(driver, element):
            print case_name+'提交成功'
        else:
            print case_name+'提交失败'
    except ValueError:
        print '元素定位失败'

def commit_presence(driver, case_name):
    time.sleep(3)
    driver.refresh()
    time.sleep(3)
    try:
        num = wait_and_find_elements_by_class_name(driver, "modal-confirm")
        if num > 2:
            print case_name+'提交成功'
        else:
            print case_name+'提交失败'
    except:
        print case_name+'提交失败'