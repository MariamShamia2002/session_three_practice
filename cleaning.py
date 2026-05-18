import pandas as pd

data_researchers=pd.read_csv('raw_data/researchers.csv')
print("Data frame shape:")
print(data_researchers.shape)
print("Data frame first 5 rows:")
print(data_researchers.head())
print("Data frame  types columns:")
print(data_researchers.dtypes)
print("Data frame last 5 rows:")
print(data_researchers.tail())
print("Data frame summary statistics:")
print(data_researchers.describe())
print("Data frame null values:")
print(data_researchers.isnull().sum())


