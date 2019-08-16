import pandas as pd

homepath = 'E:/PROJECTS/NLX/warmtetransitie'

key_df1 = pd.read_csv(homepath + '/pc6hnr20180801_gwb-vs2.csv',sep=';')
verbruik_df1 = pd.read_csv(homepath + '/Liander_Verbruiksdata_2019.csv',sep='\t')

df = key_df1[key_df1['PC6'].between('1115AC', '1115AC', inclusive=False)]

len(key_df1[key_df1['PC6'].between('1115AC', '1115AC', inclusive=True)])


df_merge_col = pd.merge(verbruik_df1, key_df1[['Buurt2018','PC6']].drop_duplicates(), left_on='POSTCODE_VAN', right_on='PC6',how='left')
print(len(df_merge_col))
print(len(verbruik_df1))
print(df_merge_col.head(5))

vc = key_df1[['Buurt2018','PC6']].drop_duplicates().PC6.value_counts()
vc2 = vc[vc > 1].index[0]
