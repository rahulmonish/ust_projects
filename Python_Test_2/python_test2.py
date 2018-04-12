import pandas as pd
import numpy as np

Location=r'D:\Dataset\Dataset.txt'

df= pd.read_csv(Location)
#print(df)

for i in range(5):
    height=df.loc[i,"Height"]
    weight=df.loc[i,"Weight"]
    bmi= weight/(height**2)
    df.loc[i,"BMI"]= bmi
    df.to_csv(Location, mode='a', header=False)
print(df)   

print("Sorting by height \n",df.sort_values(by=['Height']))

bmi=0

for i in range(5):
    if df.loc[i,"BMI"]<18:
        print(df.loc[i,"Name"], " is underweight")
    elif df.loc[i,"BMI"]>18 and df.loc[i,"BMI"]<25:
        print(df.loc[i,"Name"], " is healthy")
    elif df.loc[i,"BMI"]>25:
        print(df.loc[i,"Name"], " is underweight")
    elif df.loc[i,"BMI"]>30:
        print(df.loc[i,"Name"], " is obese")


print("Grouping by BMI\n",df.groupby('BMI').mean())