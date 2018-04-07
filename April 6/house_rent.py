# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 19:15:59 2018

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
freq = []
arr=[425,	430	,430,	435,	435,	435	,435,	435,	440	,440,
440,440,	440,	445	,445,	445	,445,	445,	450	,450,
450,	450,	450,	450,	450,	460	,460	,460	,465,	465,
465,	470,	470	,472	,475	,475,	475,	480,	480,	480,
480	,485	,490,	490	,490,	500	,500	,500,	500	,510,
510	,515,	525,	525,	525,	535,	549,	550,	570,	570,
575,	575	,580	,590,	600,	600	,600	,600	,615	,615
]
for i in range(len(arr)):
    #j=i+1
    for j in range(len(arr)):
        if arr[i]==arr[j]:
            count+=1
    #print(price[i]," \t \t", count)
   
    freq.append(count)
    count=0
plt.scatter(arr,freq)
p = np.polyfit(arr,freq,1)
plt.plot(arr,np.polyval(p,arr),"g")
plt.hist((arr,freq))