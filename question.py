import pandas as pd
df_researchers=pd.read_csv('raw_data/researchers.csv')
df_funding=pd.read_excel('raw_data/funding.xlsx')
df_publications=pd.read_json('raw_data/publications.json')
# 1 Which researcher has the highest total citations?
merged_df=pd.merge(df_researchers, df_publications ,on='researcher_id', how='left')
top_researcher = (
    merged_df
    .groupby(
        ['researcher_id', 'first_name', 'last_name']
    )['citations']
    .sum()
    .idxmax()
)
print(top_researcher)
# ('R001', 'Claire', 'Davidson')
print(df_funding.dtypes)
print(df_researchers.dtypes)
# 2 Which field received the most total funding?
merged_researchers_funding = pd.merge(df_researchers, df_funding, on='researcher_id', how='inner')
field_funding = merged_researchers_funding.groupby('field')['amount_cad'].sum()
top_field = field_funding.idxmax()
print(top_field)
# Computer Vision
# 3 Who joined earliest and is still active?
researcher=df_researchers[(df_researchers['is_active'] == True) & (df_researchers['joined_year'] == df_researchers['joined_year'].min())]
print(researcher[['first_name', 'last_name']])
# 23        Amr    Hassan