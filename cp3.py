import pandas as pd

df_xlsx=pd.read_excel('raw_data/funding.xlsx', sheet_name='Sheet1')
# print(df_xlsx.head())
# print(df_xlsx.shape)
# print(df_xlsx.dtypes)
print("Null values in amount_cad column:")
print(df_xlsx['amount_cad'].isnull().sum())
df_xlsx['amount_cad'] =(df_xlsx['amount_cad'].fillna(0))
df_xlsx =df_xlsx[df_xlsx['amount_cad'] > 0]
df_xlsx['amount_cad'] = pd.to_numeric(df_xlsx['amount_cad'], errors='coerce')
# print(df_xlsx.head(20))
print("Total funding amount in CAD:")
print(df_xlsx['amount_cad'].sum())
