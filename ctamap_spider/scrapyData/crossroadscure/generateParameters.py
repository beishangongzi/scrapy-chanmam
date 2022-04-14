import requests
import time
from datetime import date
from datetime import timedelta
from dateutil.relativedelta import relativedelta


def genP():
    """
    the prameters is the same as browser.
    brand_code=0143601861147&reputation_level=-1&page=1&size=10&sort=amount&order_by=desc&start_time=2021-10-01&end_time=2021-10-31
    :return:
    """
    # postions = {"济南市": ["长清区", "市中区", "历下区", "槐荫区", "历城区", "天桥区", "平阴县", "商河县"]}
    brand_codes = ["0143601861147"]
    reputation_levels = ['-1']
    sizes = [10]
    pages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    sorts = ["amount"]
    order_bys = ["desc"]
    start_times = ["2021-10-01"]
    end_times = ['2021-10-31']

    for brand_code in brand_codes:
        for reputation_level in reputation_levels:
            for size in sizes:
                for page in pages:
                    for sort in sorts:
                        for order_by in order_bys:
                            for start_time in start_times:
                                for end_time in end_times:
                                    yield {"brand_code": brand_code, "reputation_level": reputation_level,
                                           "size": size,
                                           "page": page,
                                           "sort": sort,
                                           "order_by": order_by,
                                           "start_time": start_time,
                                           "end_time": end_time}


if __name__ == '__main__':
    for a in genP():
        print(a)
