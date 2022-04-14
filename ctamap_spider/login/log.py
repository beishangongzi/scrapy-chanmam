import config
import selenium
import json
import time
import requests

from selenium import webdriver

def cookieProcess(cookies: dict):
    newCookies = []
    for cookie in cookies:
        name = cookie["name"]
        value = cookie["value"]
        newCookies.append({"name": name, "value": value})
    return newCookies

def serializeCookie(file):
    """
    from file load cookie
    :param file: the path of cookie file
    :return: a cookie list
    """
    fp = open(file, "r", encoding="utf-8")
    cookies = json.load(fp)
    return cookies


def seleniumLoginByCookie(url, cookies):
    driver = webdriver.Chrome(executable_path="./chromedriver")
    driver.get(url)
    driver.delete_all_cookies()
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    time.sleep(30)
    driver.refresh()

def serializeRequestHeader(file):
    """
    the content is copied from Chrome
    :param file: the path of the content of request header
    :return: request header dictary
    """
    rH = {}
    fp = open(file, "r", encoding="utf-8")
    lines = fp.readlines()
    for line in lines:
        key, value = line.split(": ")
        key = key.replace(":", "")
        rH[key] = value.strip()
    return rH




if __name__ == '__main__':
    from config.config import BASEURL, HEADER
    rH = serializeRequestHeader(HEADER)
    # r = requests.get(BASEURL, headers=rH)
    r = requests.get(BASEURL)
    html = r.content.decode("utf8", errors='ignore')
    with open("htmlWithoutHeader.html", "w", encoding="utf-8", errors='ignore') as f:
        f.write(html)



