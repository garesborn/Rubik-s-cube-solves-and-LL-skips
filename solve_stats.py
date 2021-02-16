# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 00:08:19 2021

@author: Gar
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

df = pd.read_excel('C:/Users/Gar/OneDrive/cubing/Solve_Stats.xlsx', sheet_name='solves')
solves = df['Time'].tolist()

print("")
print("Best              --", min(solves))

best3 = 60
best5 = 60
index3 = 0
index5 = 0

# Finding the Best of 5, Best 3 of 5, and their indexes
# Best 3 of 5 and later 10 of 12 remove the slowest and fastest times
for i in range(len(solves)):
    if i > 4:
        cur = solves[i-5:i]
        b5 = np.mean(cur)
        if b5 < best5:
            best5 = b5
            index5 = i
        cur.remove(min(cur))
        cur.remove(max(cur))
        b3o5 = np.mean(cur)
        if b3o5 < best3:
            best3 = b3o5
            #print(best, i, cur)
            index3 = i
print("Best 3 of 5       --", best3)
print('Best 5            --', best5)

best10 = 60
best12 = 60
index10 = 0
index12 = 0

# Finding the Best of 12, Best 10 of 12, and their indexes
for i in range(len(solves)):
    if i > 11:
        cur = solves[i-12:i]
        b12 = np.mean(cur)
        if b12 < best12:
            best12 = b12
            index12 = i
        cur.remove(min(cur))
        cur.remove(max(cur))
        b10o12 = np.mean(cur)
        if b10o12 < best10:
            best10 = b10o12
            #print(best, i, cur)
            index10 = i

print("Best 10 of 12     --", best10)
print("Best 12           --", best12)

oll = {}
pll = {}
# to plot which solves had OLL or PLL skips

# creating a list of indexes for solves with an OLL skip
for i in df.index:
    try:
        x = int(df['PLL Skip'][i])
    except:
        x = 0
    if x == 1:
        pll[df['solve #'][i]-.5] = df['Time'][i]
        
# creating a list of indexes for solves with a PLL skip
for i in df.index:
    try:
        x = int(df['OLL Skip'][i])
    except:
        x = 0
    if x == 1:
        oll[df['solve #'][i]-.25] = df['Time'][i]


avs = []
num = []
tot = 0
c = 0    

# creating averages in increments of 50, NOT USED    
for i in df.index:
    if c < 50:
        tot = tot + df['Time'][i]
        c = c + 1
    else:
        av = tot / c
        avs.append(av)
        num.append(i-50)
        c = 0
        tot = 0

# =============================================================================
#                    Plotting a Histogram of 600 Solves
# =============================================================================
ylim = 130
plt.figure(figsize=(14,6))
plt.hist(df['Time'], bins=[16,18,20,22,24,26,28,30,32,34,36,38,40])
plt.axvline(np.mean(df['Time']), 0, ylim, c = 'red')
plt.xlim(16,40)
plt.xticks(np.arange(16,40,2))
plt.ylim(0,ylim)
plt.yticks(np.arange(0,ylim,10))
plt.grid(True, axis='y')
plt.xlabel('Time (s)')
plt.ylabel('Number of Solves')
plt.title('Histogram of 600 Solves')
patches = []
patches.append(mpatches.Patch(color = 'red', label = 'Mean'))
plt.legend(handles=patches, loc = 'upper right')
plt.show()

# =============================================================================
#                     Plotting a line plot of 600 Solves
# =============================================================================
plt.figure(figsize=(12,4)) 
plt.scatter(oll.keys(),oll.values(), c = 'orange')
plt.scatter(pll.keys(),pll.values(), c = 'red')
plt.plot(df['solve #'],df['Time'])
z = np.polyfit(df['solve #'], df['Time'], 1)
p = np.poly1d(z)
plt.plot( df['solve #'], p(df['solve #']), c = 'purple', linewidth = 3)
plt.grid(True, axis = 'y')
plt.title('Cubing Solve Times vs LL Skips')
plt.xlabel('Solve Number')
plt.ylabel('Time (s)')
patches = []
patches.append(mpatches.Patch(color = 'red', label = 'PLL Skip'))
patches.append(mpatches.Patch(color = 'orange', label = 'OLL Skip'))
patches.append(mpatches.Patch(color = 'purple', label = 'fit'))
plt.legend(handles=patches, loc = 'upper right')

l = len(df['Time'])-1
print('Mean of First 200 --', np.mean(df['Time'][0:200]))
print('Mean of Last 200  --', np.mean(df['Time'][l-200:l]))
print('Improvement       --', np.mean(df['Time'][0:200])- np.mean(df['Time'][l-200:l]))
