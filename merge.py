import pandas as pd
df_researchers=pd.read_csv('raw_data/researchers.csv')
print(df_researchers.shape) # (34 rows, 11 columns)
df_funding=pd.read_excel('raw_data/funding.xlsx')
print(df_funding.shape) # (29 rows, 7 columns)
df_publications=pd.read_json('raw_data/publications.json')
print(df_publications.shape) # (61 rows, 7 columns)
merged_inner_df=pd.merge(df_researchers, df_publications ,on='researcher_id', how='inner')
merged_inner_df=pd.merge(merged_inner_df, df_funding ,on='researcher_id', how='inner')
# print(merged_inner_df.head())
print(merged_inner_df.shape) # (49 rows, 23 columns) in the inner merge
# the total number of unique researchers across all three datasets is 49, which is less than the sum of the individual dataset sizes (34 + 29 + 61 = 124) 
# due to overlapping researcher_ids across the datasets.
merged_left_df=pd.merge(df_researchers, df_publications ,on='researcher_id', how='left')
merged_left_df=pd.merge(merged_left_df, df_funding ,on='researcher_id', how='left')
# print(merged_left_df.head())
print(merged_left_df.shape) # (86 rows, 23 columns) in the left merge
# the total number of unique researchers across all three datasets is 86, which is equal to the number of researchers in the researchers dataset, 
# as the left merge retains all rows from the left dataset (researchers) and includes matching rows from the publications and funding datasets where available. 
# Researchers without matching entries in the publications or funding datasets will have NaN values in the corresponding columns. 
def clean_funding_data(df):
    df['amount_cad'] = df['amount_cad'].fillna(0)
    df = df[df['amount_cad'] > 0]
    df['amount_cad'] = pd.to_numeric(df['amount_cad'], errors='coerce')
    return df


merged_inner_df=clean_funding_data(merged_inner_df)
print(merged_inner_df.head())

merged_inner_df.to_csv('merged_inner_df.csv', index=False)