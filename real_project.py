import pandas as pd
import numpy as np
import datetime

df = pd.read_excel(r'C:\Users\Admin\Desktop\store-dataset.xlsx')

df = df.sort_values(['Product Name', 'Order Date'], ascending=[True, True])
df= df.reset_index(drop= True)
df['New Quantity']=500

l = (df['Product Name'].unique()).tolist()
d = datetime.datetime(2016, 10, 5, 18, 00)
count =0
dic = {}
df1 = pd.DataFrame()

for i in range(0,len(df['Product Name'])):
    if(l[count] == df['Product Name'][i]):
        if(d > df['Order Date'][i]):
            df['New Quantity'][i]= df['New Quantity'][i]  - df['Quantity'][i]
            df['New Quantity'][i+1]=df['New Quantity'][i]
            df1 = df1.append(df.iloc[i,:])
    else:
        count+=1

count=0
df2 = pd.DataFrame()
l2 = (df1['Product Name'].unique()).tolist()

for i in range(0,len(df1['Product Name'])-1):
    if l2[count]!=df1['Product Name'].iloc[i+1]:
        df2 = df2.append(df1.iloc[i,:])
        count+=1

        
