# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 22:05:18 2018

@author: ATIV 9 Lite
"""
import numpy as np

# ----stocks.py를 실행해서 get_data() 함수 얻어야함------

def strategy(d2, k=0.5):
    d = d2.copy()
    d.insert(len(d.columns), 'range', d['high']-d['low'])
    
    prev_range = d['range'].shift(1)
    sell_price = d['open'].shift(-1)
    buy_price = round((d['open'] + prev_range * k)/5.0)*5
    bool = d['high'] >= buy_price
    bool = bool.astype(int)
    
    daily_profit = bool * ((sell_price - buy_price) / buy_price - 0.15/100)
    d['profit'] = np.nan
    k = len(d.columns) - 1
    d.iloc[0,k] = 1  #여기서 d['profit'][0]로 하면 SettingWithCopyWarning이 뜸
    for i in range(1,len(d['profit'])):
        d.iloc[i,k] = d.iloc[i-1,k] * (1 + daily_profit[i]) # 여기도
    d = d.dropna()
    return d['profit']