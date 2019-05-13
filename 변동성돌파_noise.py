# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 22:05:18 2018

@author: ATIV 9 Lite
"""
import numpy as np
import pandas as pd
# ----stocks.py를 실행해서 get_data() 함수 얻어야함------

def strategy_noise(d2, days=3):
    d = d2.copy()
    d.insert(len(d.columns), 'range', d['high']-d['low'])
    
    prev_range = d['range'].shift(1)
    sell_price = d['open'].shift(-1)
    
    noise = 1 - abs(d['open']-d['close'])/abs(d['high']-d['low'])
    d.insert(len(d.columns), 'noise3', noise.shift(1).rolling(days).mean())
    d = d.dropna()    
    
    buy_price = round((d['open'] + prev_range * d['noise3'])/5.0)*5
    buy_price = buy_price.dropna()
    bool = d['high'] >= buy_price
    bool = bool.astype(int)
    daily_profit = bool * ((sell_price - buy_price) / buy_price - 0.15/100)
    daily_profit = daily_profit.dropna()
   
    pf = pd.Series(index=d.index)
    pf[0] = 1
    for i in range(1,len(pf)-1):
        pf[i] = pf[i-1] * (1 + daily_profit[i])
    pf = pf.dropna()
    return pf