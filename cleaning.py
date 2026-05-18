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

print("Data frame duplicates:")
print(df.duplicated().sum())
print("Data frame publications count:")
print(df['publications_count'].value_counts())
print("Data frame h-index summary statistics:")
print(df['h_index'].describe())

active_researchers = df[df['is_active'] == True]
print("Active researchers:")
print(active_researchers.shape)
high_impact_researchers = df[(df['is_active'] == True) & (df['h_index'] > 15)]
print("High impact researchers:")
high_impact_researchers=high_impact_researchers.sort_values('joined_year', ascending=True)
print(high_impact_researchers['last_name'].str[0])
# hidden word :DATA OPENS DOORS
df_json=pd.read_json('raw_data/publications.json')
print (df_json.head())
print(df_json.shape)
print(df_json.dtypes)
paper_most_citations = df_json.groupby('title')['citations'].max().sort_values(ascending=False).head(1)
print("Paper with most citations:")
print(paper_most_citations)
# Data Opens Doors: A Manifesto for Open Research    9999
