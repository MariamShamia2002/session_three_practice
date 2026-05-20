import pandas as pd
df_json=pd.read_json('raw_data/publications.json')
print (df_json.head())
print(df_json.shape)
print(df_json.dtypes)
paper_most_citations = df_json.groupby('title')['citations'].max().sort_values(ascending=False).head(1)
print("Paper with most citations:")
print(paper_most_citations)
# Data Opens Doors: A Manifesto for Open Research    9999