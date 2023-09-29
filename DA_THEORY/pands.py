import numpy as np
import pandas as pd
import numpy as np
s=pd.Series([3,4,3,77,44])
print(s)

myindex=['USA','canada','Mexico']
mydata=[1776,1867,1821]

#only index,no labels
myser=pd.Series(data=mydata)
print(myser)

#now a label index
myser=pd.Series(data=mydata,index=myindex)
print(myser)
print()

#Create a series from a dictionary
ages = {'sammy':5,'Frank':10,'spike':7}
ser = pd.Series(ages)
print(ser)
print()

# Convert dict into pandas
q1={'japan':80,'china':450,'India':200,'USA':250}
q2={'Brazil':100,'china':500,'India':210,'USA':260}
sales_q1 = pd.Series(q1)
sales_q2 = pd.Series(q2)

print(sales_q1)
print(sales_q1['japan'])
print(sales_q1[0])

np.all