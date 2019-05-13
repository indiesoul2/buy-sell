# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 23:22:22 2018

@author: ATIV 9 Lite
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# d를 get_data()로 얻어옴

cagr = []; mdd= []; index=[]

for i in np.arange(0.1, 1.05, 0.05):
    c, m = result(strategy(d, i))
    cagr.append(c); mdd.append(m); 
    index.append('*{}'.format(round(i*100)/100))
    
cagr2 = pd.Series(cagr, index=index)
mdd2 = pd.Series(mdd, index=index)

cagrMdd = pd.DataFrame({'CAGR':cagr2, 'MDD':mdd2})

#이제 그래프!
plt.bar(cagrMdd.index,cagrMdd['CAGR'], 0.35, color='b', label = 'CAGR')
plt.ylabel('CAGR (%)')
plt.legend(loc='upper center')
plt.twinx()
plt.plot(cagrMdd.index, cagrMdd['MDD'], '-or', label='MDD')
plt.ylabel('MDD (%)')
plt.legend()
