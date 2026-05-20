import pandas as pd

df_funding=pd.read_excel('raw_data/funding.xlsx', sheet_name='Sheet1')
# print(df_funding.head())
# print(df_funding.shape)
# print(df_funding.dtypes)
# print("Null values in amount_cad column:")
# print(df_funding['amount_cad'].isnull().sum())
# df_funding['amount_cad'] =(df_funding['amount_cad'].fillna(0))
# df_funding =df_funding[df_funding['amount_cad'] > 0]
# df_funding['amount_cad'] = pd.to_numeric(df_funding['amount_cad'], errors='coerce')
# print(df_funding.head(20))
# print("Total funding amount in CAD:")
# print(df_funding['amount_cad'].sum())

def clean_funding_data(df):
    df['amount_cad'] = df['amount_cad'].fillna(0)
    df = df[df['amount_cad'] > 0]
    df['amount_cad'] = pd.to_numeric(df['amount_cad'], errors='coerce')
    return df
print ("Total funding amount in CAD after cleaning:")
print (clean_funding_data(df_funding)['amount_cad'].sum())
# Total funding amount in CAD after cleaning:
# 2024000.0
