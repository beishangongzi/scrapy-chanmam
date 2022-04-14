
# -*- coding: utf-8 -*-
"""
2019.12.10

firefox browser v71.0 x64
geckodriver v0.26.0 x64
python 3.7.4
"""

import os
import logging

from scipy.stats import logistic

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.remote_connection import LOGGER
LOGGER.setLevel(logging.WARNING)

ROOT = os.getcwd()

def smooth_move(bar_length = 396): #bar_length = slide bar pixel
    x = [0.01,0.02,0.3,0.7,0.8,0.9]
    y = list(map(logistic.cdf, x))
    begin, end = y[0], y[-1]
    Y = list(map(lambda a: (a - begin)/(end - begin), y))
    gaps = []
    for i in range(len(Y)):
        if i != 0:
            gaps.append(Y[i] - Y[i-1])
    return list(map(lambda b: int(b*bar_length*1.2), gaps))


def ask4cookie(webdriver_path, tb_username, tb_password):
    options = Options()
    options.add_argument('--headless')
    print('模拟登陆中')
    browser = Firefox(executable_path = webdriver_path, options = options)

    try:
        browser.get('https://its.amap.com/welcome#/?redirect=%2Fdashboard')
    except:
        raise Exception('无法访问its.amap.com，请检查网络连接。')

    with open(os.path.join(ROOT, 'javascriptFirefox.js'), 'r') as f:
        cheating_js = f.read()
        browser.execute_script(cheating_js)

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div.index-header-right')
            )
        )
    browser.find_elements_by_css_selector('div.index-header-right > span')[1].click()

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#nc_1_n1z')
            )
        )
    browser.find_element_by_css_selector('input.username').send_keys(tb_username)
    browser.find_element_by_css_selector('input.password').send_keys(tb_password)
    knot = browser.find_element_by_css_selector('#nc_1_n1z')
    intervals = smooth_move()

    ActionChains(browser).click_and_hold(knot).perform()
    for interval in intervals:
        ActionChains(browser).move_to_element_with_offset(knot, xoffset=interval, yoffset=0).perform()
    ActionChains(browser).release(knot).perform()
    browser.find_element_by_css_selector('#login_submit').click()

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div.currentVerySmoothExponent')
            )
        )

    cookies = {}
    for i in browser.get_cookies():
        cookies[i["name"]] = i["value"]
    browser.quit()

    #cookie expires in 10 hrs
    if 'userName' in cookies.keys():
        cookie = ''
        for k, v in cookies.items():
            cookie += '{}={};'.format(k, v)
        print('登陆成功')
        return cookie
    else:
        raise Exception('登录its.amap.com失败。请检查账号有效性。')

cookies = ask4cookie()
