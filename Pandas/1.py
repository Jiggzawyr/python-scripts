import pandas as pd

s1 = pd.Series([1,2,3,4,5,6])
print(s1)

s2 = pd.Series([1,2,3],index=['a','b','c'])
print(s2)

s3 = pd.Series({'a' : 100, 'b' : 200, 'c' : 300})
print(s3)

s4 = pd.Series({'a' : 100, 'b' : 200, 'c' : 300},index=['d','c','b','a'])
print(s4)

s5 = pd.Series([1,2,3,4,5,6])
print(s5[3])

s6 = pd.Series([1,2,3,4,5,6])
print(s6[:4])

s7 = pd.Series([1,2,3,4,5,6])
print(s7[-3:])

s8 = pd.Series([1,2,3,4,5,6])
print(s8 + 5)

s9 = pd.Series([1,2,3,4,5,6])
s10 = pd.Series([1,2,3,4,5,6])
print(s9 + s10)