# --*-- coding:utf8 --*--
# 进入填表页面
import selenium.webdriver
from linklab_test_case.action.web_service import *


def enter_subform(driver, linklab_url):
    driver.get(linklab_url + '/project/user/#/')
    wait_and_find_elements_by_link_text(driver, '进入项目')[3].click()
    wait_and_find_elements_by_class_name(driver, 'navItem-title')[2].click()
    wait_and_find_elements_by_class_name(driver, 'collect_modules')[0].click()
    all_hand = driver.window_handles
    driver.switch_to.window(all_hand[-1])

