import json
import requests
import time
import os
from urllib.parse import urlparse
from config.config import DATAFILE
from exeption.Exception import AuthFailedException, UrlISNoneException


def isLogin(code):
    if code == 40000:
        raise AuthFailedException(code)
    else:
        pass


class Scrapy:
    def __init__(self, url=None, path=None, headers=None, sleep=1):
        """

        :param url: the scheme, host and path of url
        :param path: the path to storage the json data
        :param headers: request headers
        :param sleep: default sleep 1s/request
        """
        self.url = url
        if path is None:
            self.path = self.setPath()
        else:
            self.path = path
        self.headers = headers
        self.sleep = sleep

    def getData(self, params):
        """
        call requests.get()
        there is a check for authentication, if no authentication, raise AuthFailedException
        for safety, set thread sleep
        :param params: -> params. is a dictionary of query string.
        :return: request response
        """
        if self.url is None:
            raise UrlISNoneException
        time.sleep(self.sleep)
        data = requests.get(url=self.url, headers=self.headers, params=params)
        res = data.json()
        print(data.url)
        if res["errCode"] == 0:
            print("success")
            return res
        else:
            print(res)
            raise AuthFailedException

    def postData(self, postData=None, postJson=None):
        """
        call requests.post()
        there is a check for authentication, if no authentication, raise AuthFailedException
        for safety, set thread sleep
        :param postData: -> data
        :param postJson: -> json
        :return: request response
        """
        if self.url is None:
            raise UrlISNoneException
        time.sleep(1)
        data = requests.post(url=self.url, headers=self.headers, json=postJson, data=postData)
        res = data.json()
        # try:
        #     isLogin(res["code"])
        # except AuthFailedException as e:
        #     print(e)
        # except:
        #     pass
        return res

    def write2File(self, data, mode="a+"):
        """
        dump data to file
        :param data:
        :return:
        """
        dirName = os.path.dirname(self.path)
        os.makedirs(dirName, exist_ok=True)
        with open(self.path, mode, encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)
            f.write("\n")

    def setHeadersFromFile(self, file):
        """
        set Headers From File
        :param file:
        :return:
        """
        rH = {}
        fp = open(file, "r", encoding="utf-8")
        lines = fp.readlines()
        for line in lines:
            key, value = line.split(": ")
            key = key.replace(":", "")
            rH[key] = value.strip()
        self.headers = rH

    def setHeadersAuto(self):
        """
        Automatically obtain request headers
        :return:
        """
        self.headers = None

    def setPath(self, fileFormat="json"):
        """
        set the storage path
        :return
        """
        return str(DATAFILE) + urlparse(self.url).path[0:-1] + "." + fileFormat





