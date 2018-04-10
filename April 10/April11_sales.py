from pandas import DataFrame, read_csv
import matplotlib.pyplot 
import pandas as pd #this is how I usually import pandas
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number
import os
import numpy as np

Location= r'C:\Users\user\Downloads\100-Sales-Records\100 Sales Records.csv'
df1 = pd.read_csv(Location)
print("Columns are \n\n",df1.columns.values)
print("The first ten values are ",df1.head(10))
df1['Total Profit'].plot()
print("The item with more than 1000000 profit is ")
for index, row in df1.iterrows():
    if row['Total Cost']> 1000000:
        print (row['Item Type'])