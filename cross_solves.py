# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 19:35:05 2021

@author: Gar
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

mdf = pd.read_excel('C:/Users/Gar/OneDrive/cubing/Solve_Stats.xlsx', sheet_name='cross move counts')
sdf = pd.read_excel('C:/Users/Gar/OneDrive/cubing/Solve_Stats.xlsx', sheet_name='cross solves')

print(np.mean(sdf['time']))
print(np.mean(mdf['moves']))
patches  = []


# =============================================================================
#                      Line plot of timed Cross solves
# =============================================================================
plt.figure(figsize=(12,4))
plt.plot(sdf['solve #'],sdf['time'])
plt.plot(sdf['solve #'], [np.mean(sdf['time'])]*len(sdf['solve #']), c = 'red', linewidth = 3)
plt.grid(True, axis = 'y')
plt.title('Cubing Cross Solve Times')
plt.xlabel('Solve Number')
plt.ylabel('Time (s)')
patches.append(mpatches.Patch(color = 'red', label = 'Mean'))
plt.legend(handles=patches, loc = 'upper right')