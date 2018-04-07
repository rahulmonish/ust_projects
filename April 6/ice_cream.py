# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 19:08:23 2018

@author: user
"""
import numpy as np
import matplotlib.pyplot as plt
x = np.array([14.2,16.4,11.9,15.2,18.5,22.1,19.4,25.1])
y = np.array([215,325,185,332,406,522,412,614])

plt.scatter(x,y)
p = np.polyfit(x,y,1)
plt.plot(x,np.polyval(p,x),"g")