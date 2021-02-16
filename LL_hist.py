# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 15:42:06 2021

@author: Gar
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.ticker import PercentFormatter

df = pd.read_excel('C:/Users/Gar/OneDrive/cubing/Solve_Stats.xlsx', sheet_name = 'LL')

ll2 = []
ll3 = []
ll4 = []
ll5 = []

# compiling solve times into lists for each # of LL algs
for i in df.index:
    if df['LL_algs'][i] == 2:
        ll2.append(df['time'][i])
    elif df['LL_algs'][i] == 3:
        ll3.append(df['time'][i])
    elif df['LL_algs'][i] == 4:
        ll4.append(df['time'][i])
    elif df['LL_algs'][i] == 5:
        ll5.append(df['time'][i])

# Finding % chance of solving LL with each # of algs
print('odds of 2 look:', len(ll2)/2.5)        
print('odds of 3 look:', len(ll3)/2.5)
print('odds of 4 look:', len(ll4)/2.5)
print('odds of 5 look:', len(ll5)/2.5)
print('Mean of Solves', np.mean(df['time']))

#compiling a list of averages
avs = [np.mean(ll2),np.mean(ll3),np.mean(ll4),np.mean(ll5), np.mean(df['time'])]

# =============================================================================
#               Plotting overlapped Histogram
# =============================================================================
plt.figure(figsize=(14,6))
plt.grid(True,axis='y')
plt.title('Histogram of Solve times based on the Number of Algorithms used to Solve last Layer')
plt.hist(ll3, bins=[16,18,20,22,24,26,28,30,32,34])
plt.hist(ll3, bins=[16,18,20,22,24,26,28,30,32,34])
plt.hist(ll4, bins=[16,18,20,22,24,26,28,30,32,34])
plt.hist(ll5, bins=[16,18,20,22,24,26,28,30,32,34])
plt.hist(ll2, bins=[16,18,20,22,24,26,28,30,32,34])
plt.xticks(np.arange(16,35,2))
plt.xlabel('Solve time (s)')
plt.show()


# =============================================================================
#               Plotting 2D Histogram of Times by LL Algs
# =============================================================================
plt.figure(figsize=(14,4))
plt.title('2D Histogram of Solve times based on the Number of Algorithms used to Solve last Layer')
plt.hist2d(df['time'],df['adj'],[np.arange(16,36,1),np.arange(1.5,6.5,1)], cmap='binary')
mx = .245
mn = 0
c = 'red'
for i in avs:
    if i == np.mean(df['time']):
        mn = 0
        mx = 1
        c = 'green'
    plt.axvline(i, mn, mx, c = c)
    mn = mn + .25
    mx = mx + .25

patches = []

plt.yticks(np.arange(2,6,1))
plt.xticks(np.arange(16,35,1))
plt.xlabel('Solve time (s)')
plt.ylabel('Number of Algs to Solve LL')
patches.append(mpatches.Patch(color = 'red', label = 'Bin Mean'))
patches.append(mpatches.Patch(color = 'green', label = 'Overall Mean'))
plt.legend(handles=patches, loc = 'upper left')
plt.show()


# =============================================================================
#               Plotting Hist of # of LL Algs used
# =============================================================================
data = df['adj'].tolist()
plt.figure(figsize=(3,4))
#plt.yticks(np.arange(2,6,1))
plt.ylim(1.5,5.5)
plt.hist(data,np.arange(1.5,6.5,1), weights=np.ones(len(data)) / len(data),orientation='horizontal', color='black')
plt.gca().xaxis.set_major_formatter(PercentFormatter(1))
plt.xticks(np.arange(0,.6,.1))
plt.grid(True, axis ='x')
plt.tick_params(axis='y',left=False,labelleft=False)
plt.xlabel('Percentage of Solves')

#Difference of between average and 2 look LL average
print('Possible improvement:', avs[4]-avs[0])
