import pandas as pd

df1 = pd.DataFrame({'Name' : ['Sam','Anne','Matt'], 'Marks' : [99,44,81]})
print(df1)

csv_name = "iris.csv"
iris = pd.read_csv(f"{csv_name}")

print(iris.head())
print(iris.tail())
print(iris.shape)
print(iris.describe())

print(iris.iloc[0:3,0:2])
print(iris.loc[5:10,('Petal.Length','Species')])

print(iris.drop('Species',axis=1))
print(iris.drop([1,2,3],axis=0))

print(iris.mean())
print(iris.median())
print(iris.min())
print(iris.max())

def half(s):
    return s*0.5

print(iris[['Sepal.Length','Sepal.Width']].apply(half))

print(iris['Species'].value_counts())
print(iris.sort_values(by='Sepal.Length'))