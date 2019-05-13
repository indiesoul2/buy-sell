# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 00:06:36 2018

@author: ATIV 9 Lite
"""
cagr = []; mdd= []; index=[]

for i in range(1,21):
    c, m = result(strategy_noise(d, i))
    cagr.append(c); mdd.append(m); 
    index.append(i)
    
cagr2 = pd.Series(cagr, index=index)
mdd2 = pd.Series(mdd, index=index)

cagrMdd = pd.DataFrame({'CAGR':cagr2, 'MDD':mdd2})

plt.bar(cagrMdd.index,cagrMdd['CAGR'], 0.35, color='b', label = 'CAGR')
plt.ylabel('CAGR (%)')
plt.legend(loc='upper center')
plt.ylim(50,90)
plt.xticks(range(1,21))
plt.twinx()
plt.plot(cagrMdd.index, cagrMdd['MDD'], '-or', label='MDD')
plt.ylabel('MDD (%)')
plt.legend()
plt.ylim(0,40)
