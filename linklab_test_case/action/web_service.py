import os.path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def wait_and_find_element(driver, element_name, by=By.ID):
    if by == By.ID:
        return WebDriverWait(driver, 20, poll_frequency=1).until(lambda x: x.find_element_by_id(element_name))
    elif by == By.XPATH:
        return WebDriverWait(driver, 20, poll_frequency=1).until(lambda x: x.find_element_by_xpath(element_name))
    elif by == By.TAG_NAME:
        return WebDriverWait(driver, 20, poll_frequency=1).until(lambda x: x.find_element_by_tag_name(element_name))
    elif by == By.LINK_TEXT:
        return WebDriverWait(driver, 20, poll_frequency=1).until(lambda x: x.find_element_by_link_text(element_name))
    elif by == By.NAME:
        return WebDriverWait(driver, 20, poll_frequency=1).until(lambda x: x.find_element_by_name(element_name))
    elif by == By.CLASS_NAME:
        return WebDriverWait(driver, 20, poll_frequency=1).until(lambda x: x.find_element_by_class_name(element_name))
    elif by == By.PARTIAL_LINK_TEXT:
        return WebDriverWait(driver, 20, poll_frequency=1).until(lambda x: x.find_element_by_partial_link_text(element_name))
    elif by == By.CSS_SELECTOR:
        return WebDriverWait(driver, 20, poll_frequency=1).until(lambda x: x.find_element_by_css_selector(element_name))
    else:
        return None


def wait_and_find_element_by_id(driver, element_name):
    return wait_and_find_element(driver, element_name, By.ID)


def wait_and_find_element_by_name(driver, element_name):
    return wait_and_find_element(driver, element_name, By.NAME)


def wait_and_find_element_by_class_name(driver, element_name):
    return wait_and_find_element(driver, element_name, By.CLASS_NAME)


def wait_and_find_element_by_xpath(driver, element_name):
    return wait_and_find_element(driver, element_name, By.XPATH)


def wait_and_find_element_by_link_text(driver, element_name):
    return wait_and_find_element(driver, element_name, By.LINK_TEXT)


def wait_and_find_element_by_css_selector(driver, element_name):
    return wait_and_find_element(driver, element_name, By.CSS_SELECTOR)


def wait_and_find_element_by_tag_name(driver, element_name):
    return wait_and_find_element(driver, element_name, By.TAG_NAME)


def wait_and_find_element_by_partial_link_text(driver, element_name):
    return wait_and_find_element(driver, element_name, By.PARTIAL_LINK_TEXT)


def wait_and_find_elements(driver, element_name, by=By.ID):
    if by == By.ID:
        return WebDriverWait(driver, 20, poll_frequency=1).until(lambda x: x.find_elements_by_id(element_name))
    elif by == By.XPATH:
        return WebDriverWait(driver, 20, poll_frequency=1).until(lambda x: x.find_elements_by_xpath(element_name))
    elif by == By.TAG_NAME:
        return WebDriverWait(driver, 20, poll_frequency=1).until(lambda x: x.find_elements_by_tag_name(element_name))
    elif by == By.LINK_TEXT:
        return WebDriverWait(driver, 20, poll_frequency=1).until(lambda x: x.find_elements_by_link_text(element_name))
    elif by == By.NAME:
        return WebDriverWait(driver, 20, poll_frequency=1).until(lambda x: x.find_elements_by_name(element_name))
    elif by == By.CLASS_NAME:
        return WebDriverWait(driver, 20, poll_frequency=1).until(lambda x: x.find_elements_by_class_name(element_name))
    elif by == By.PARTIAL_LINK_TEXT:
        return WebDriverWait(driver, 20, poll_frequency=1).until(lambda x: x.find_elements_by_partial_link_text(element_name))
    elif by == By.CSS_SELECTOR:
        return WebDriverWait(driver, 20, poll_frequency=1).until(lambda x: x.find_elements_by_css_selector(element_name))
    else:
        return None


def wait_and_find_elements_by_id(driver, element_name):
    return wait_and_find_elements(driver, element_name, By.ID)


def wait_and_find_elements_by_name(driver, element_name):
    return wait_and_find_elements(driver, element_name, By.NAME)


def wait_and_find_elements_by_class_name(driver, element_name):
    return wait_and_find_elements(driver, element_name, By.CLASS_NAME)


def wait_and_find_elements_by_xpath(driver, element_name):
    return wait_and_find_elements(driver, element_name, By.XPATH)


def wait_and_find_elements_by_link_text(driver, element_name):
    return wait_and_find_elements(driver, element_name, By.LINK_TEXT)


def wait_and_find_elements_by_css_selector(driver, element_name):
    return wait_and_find_elements(driver, element_name, By.CSS_SELECTOR)


def wait_and_find_elements_by_tag_name(driver, element_name):
    return wait_and_find_elements(driver, element_name, By.TAG_NAME)


def wait_and_find_elements_by_partial_link_text(driver, element_name):
    return wait_and_find_elements(driver, element_name, By.PARTIAL_LINK_TEXT)