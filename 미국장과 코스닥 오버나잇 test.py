# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 17:16:22 2018

@author: ATIV 9 Lite
"""
## 미국장과 코스닥 오버나잇 테스트
import pandas as pd
import pandas_datareader as web
import datetime
import matplotlib as plt
import numpy as np

# 데이터 준비
start = datetime.datetime(2001,1,1); end = datetime.datetime(2018,2,22)
SnP = web.DataReader('^GSPC','yahoo', start, end) # S&P 500 데이터
del SnP['Close']; del SnP['Volume']
SnP.columns = ['open','high','low','close']
s = SnP.copy()

kq = pd.read_csv('kosdaq.csv', index_col='date', parse_dates=True)
kq = kq.sort_index(ascending=1)
q = kq.copy()

# 상관관계 분석
q['overnight'] = 100*(q['open'].shift(-1)/q['close'] - 1)
s['change'] = s['close'].pct_change()

q['profit']=1
for i in range(1,len(q)):
   q.iloc[i,6] = q.iloc[i-1,6]*(1+q.iloc[i-1,5]/100)
   
x1 = pd.concat([s['change'],q['overnight']], axis=1, join='inner')
x1 = x1.dropna()
snp = x1['change'].values
overnight = x1['overnight'].values
fit = np.polyfit(snp, overnight, deg=1)

fig, ax = plt.subplots() # 선형회귀 그래프 그리기
ax.scatter(snp, overnight)
ax.axhline(y=0, color='b', linestyle='--')
ax.axvline(x=0, color='b', linestyle='--')
ax.plot(snp, snp*fit[0] + fit[1], color='red')
ax.set(title='linear regression', xlabel='S&P 500 daily change (%)', ylabel='KOSDAQ overnight (%)')

import scipy.stats # 선형회귀 결과 데이터
slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(snp, overnight)
Rsquare = r_value ** 2
print(Rsquare)

## 미국장이 하락하면 오버나잇 수익률이 어떻게 되나?

q2 = q['profit']; s2 = s['close']
fig, ax1 = plt.subplots() 
ax1.plot(q2, label='overnight'); ax1.set_yscale('log')
ax2 = ax1.twinx()
ax2.plot(s2, color='red', label='S&P 500')
ax1.legend();ax2.legend(loc='upper center')
ax1.set(title='2001.1 ~ 2018.2')

fig, ax1 = plt.subplots() #하락한 구간들만 확대해보
ax1.plot(q2.loc['2001-1-1':'2003-1-1'], label='overnight')
ax2 = ax1.twinx()
ax2.plot(s2.loc['2001-1-1':'2003-1-1'], color='red', label='S&P 500')
ax1.legend();ax2.legend()
ax1.set(title='2001.1 ~ 2003.1')

fig, ax1 = plt.subplots()
ax1.plot(q2.loc['2008-1-1':'2009-4-1'], label='overnight'); ax1.set_yscale('log')
ax2 = ax1.twinx()
ax2.plot(s2.loc['2008-1-1':'2009-4-1'], color='red', label='S&P 500')
ax1.legend();ax2.legend()
ax1.set(title='2008.1 ~ 2009.4')

fig, ax1 = plt.subplots()
ax1.plot(q2.loc['2015-1-1':'2016-1-1'], label='overnight'); ax1.set_yscale('log')
ax2 = ax1.twinx()
ax2.plot(s2.loc['2015-1-1':'2016-1-1'], color='red', label='S&P 500')
ax1.legend();ax2.legend()
ax1.set(title='2015.1 ~ 2015.12')