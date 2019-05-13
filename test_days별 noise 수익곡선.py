# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 01:10:55 2018

@author: ATIV 9 Lite
"""

for i in [1,3,7,13,20]:
    d2 = d.copy()
    profit = strategy_noise(d2, i)
    plt.plot(profit.index, profit, label='{} days noise'.format(i))
    
plt.legend()