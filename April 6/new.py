import numpy as np
import matplotlib.pyplot as plt
freq = []
price=[1.45,2.20,0.75,1.23,1.25,1.25,3.09,1.99,2.00,0.78,1.32,2.25,3.15,3.85,0.52,0.99,1.38,1.75,1.22,1.75]
price.sort()
count=0
for i in range(len(price)):
    #j=i+1
    for j in range(len(price)):
        if price[i]==price[j]:
            count+=1
    #print(price[i]," \t \t", count)
   
    freq.append(count)
    count=0
print(len(freq),len(price))
plt.hist((price,freq))
#print (price)