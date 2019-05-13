# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 21:15:09 2018

@author: ATIV 9 Lite
"""

import datetime
import requests
from io import StringIO
from pandas.io.common import urlencode
import pandas as pd

BASE = 'http://finance.google.com/finance/historical'


def get_params(symbol, start, end):
    params = {
        'q': symbol,
        'startdate': start.strftime('%Y/%m/%d'),
        'enddate': end.strftime('%Y/%m/%d'),
        'output': "csv"
    }
    return params


def build_url(symbol, start, end):
    params = get_params(symbol, start, end)
    return BASE + '?' + urlencode(params)

def get_data(code='233740', start=datetime.datetime(2010,1,1), end=datetime.datetime.today()):
    sym = 'KRX:'+code
    url = build_url(sym, start, end)

    data = requests.get(url).text
    data = pd.read_csv(StringIO(data), index_col='Date', parse_dates=True)
    data = data.sort_index(ascending=1)
    data=data.dropna()
    data.columns = ['open','high','low','close','volume']
    return data