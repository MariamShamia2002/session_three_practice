import pandas as pd
#creat data frame
df=pd.read_csv('raw_data/researchers.csv')
print("Data frame shape:")
print(df.shape)
print("Data frame first 5 rows:")
print(df.head())
print("Data frame  types columns:")
print(df.dtypes)
print("Data frame last 5 rows:")
print(df.tail())
print("Data frame summary statistics:")
print(df.describe())
print("Data frame null values:")
print(df.isnull().sum())


