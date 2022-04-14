import os.path

import requests
from scrapyData.crossroadscure.generateParameters import genP
from config.config import HEADER
from scrapyData.scrapy import Scrapy

crossRankingListUrl = "https://ct.amap.com/diagnosis/crossDiagnosis/crossRankingList"
timespanUrl = "https://ct.amap.com/diagnosis/crossDiagnosis/inter/timespan"
interRightturnUrl = "https://ct.amap.com/diagnosis/crossDiagnosis/interRightturn"
chanmammaUrl = "https://api-service.chanmama.com/v1/brand/detail/authors"


timespanDict = {
    "早晚高峰": {"name": "PEAK", "id": 0},
    "早高峰": {"name": "M_PEAK", "id": 1},
    "晚高峰": {"name": "E_PEAK", "id": 2},
    "平峰": {"name": "F_PEAK", "id": 3},
    "凌晨": {"name": "MORNIN", "id": 4},
    "夜间": {"name": "NIGHT", "id": 5},
    "全天": {"name": "ALL_DAY", "id": 6},
}


def scrapy(s: Scrapy):
    params = genP()
    for p in params:
        qi = getCrossRankingListUrl(s, queryInfo=p)
        print(qi)
        setPath(s, p)
        print(s.url)
        data = s.getData(qi)
        print(data)
        s.write2File(data)
        # qi = getInterRightturnUrl(s, queryInfo=p)
        # setPath(s, p)
        # data = s.getData(qi)
        # s.write2File(data)
        #
        # if (p["timespan"] == "早高峰"):
        #     for type in range(1, 3):
        #         qi = getTimespanUrl(s, queryInfo=p, type=type)
        #         setPath(s, p)
        #         s.path = os.path.dirname(s.path)+ f"/{type}/" + os.path.basename(s.path)
        #         data = s.getData(qi)
        #         s.write2File(data)
        #
        # print("-----------")
#

def getTimespanUrl(s: Scrapy, queryInfo: dict, type):
    """
    adcode=370100
    district=370114
    ds=202109
    dss=202109
    timespan=1,2
        1,2

    dimension=MONTH
    isPage=0
    type=2
        1 or 2
    :param s:
    :param queryInfo:
    :return:
    """
    s.url = timespanUrl
    params = {"adcode": 370100}
    params["district"] = queryInfo["postion"]
    params["ds"] = queryInfo["date"]
    params["dss"] = queryInfo["date"]
    params["timespan"] = "1,2"
    params["dimension"] = queryInfo["dimension"]
    params["type"] = type
    params["isPage"] = 0
    return params


def getCrossRankingListUrl(s: Scrapy, queryInfo: dict):
    """
        adcode 市级行政代码
        district 县级行政代码
        ds 起始日期
            天维度：20201008
            月维度：202108
        dss 结束日期
            天维度：20201008
            月维度：202108
        timespan 时间跨度
            PEAK 早晚高峰
            M_PEAK 早高峰
            E_PEAK 晚高峰
            F_PEAK 平峰
            MORNIN 凌晨
            NIGHT 夜间
            ALL_DAY 全天

        dimension  时间维度
            DAY
            MONTH
    :param s:
    :param queryInfo:
    :return:
    """
    s.url = chanmammaUrl
    return queryInfo


def getInterRightturnUrl(s: Scrapy, queryInfo: dict):
    """
        adcode=370100
        district=370114
        ds=202109
        dss=202109
        timespan=3
            这个是和时间有关系的
        dimension=MONTH
        isPage=0
    :param s:
    :param queryInfo:
    :return:
    """
    s.url = interRightturnUrl
    params = {"adcode": 370100}
    params["district"] = queryInfo["postion"]
    params["ds"] = queryInfo["date"]
    params["dss"] = queryInfo["date"]
    params["timespan"] = timespanDict[queryInfo["timespan"]]["id"]
    params["dimension"] = queryInfo["dimension"]
    params["isPage"] = 0
    return params

def setPath(s: Scrapy, p: dict):
    path = s.setPath()
    #{"postion": postion, "timespan": timespan, "dimension": dimension, "date": res}
    name = "-".join(map(str, p.values()))
    s.path = path + "/" + name + ".json"

if __name__ == '__main__':

    s = Scrapy(url=chanmammaUrl, sleep=1)
    s.setHeadersFromFile(HEADER)
    scrapy(s)
