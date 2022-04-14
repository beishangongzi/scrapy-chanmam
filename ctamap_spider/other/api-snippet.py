def historyRoadRanking(cookie, params):
    headers = {'Cookie':cookie,
               'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'}
    url = 'https://its.amap.com/judge/road/roadHistoryJudgeList'
    '''
    params = {
            'sort':'IDX',
            'roadClass':'ALL',
            'roadLength':'',
            'dayType':day_type,
            'timePeriod':time_period,
            'name':'',
            'dateRange':'CUSTOM_DATE',
            'date':'{}@{}'.format(timestamp, timestamp),
            'size':100,
            'district':district,
            'linksType':4,
            'adcode':'371300',
            'page':1
        }
    '''
    try:
        r = requests.get(url, params = params, headers = headers)
        if r.status_code == 200:
            return r.json()
        else:
            raise Exception('访问its.amap.com接口失败，请检查账号有效性。')
    except:
        print('爬取historyRoadRanking失败，请检查网络连接。')
        return []
