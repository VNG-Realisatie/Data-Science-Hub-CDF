''' Dit script is ontwikkeld vanuit de DataScienceHub, onderdeel van VNG-realisatie
als deel van de CommonDataFactory.

Ontwikkelaar: Kees Kraan
'''
# Import libraries
import pandas as pd

# Define constants
datafiles = ['Stedin_Verbruiksdata_2019','Liander_Verbruiksdata_2019','Enexis_Verbruiksdata_2019']
keyfile = '../Data/pc6hnr20180801_gwb-vs2.csv'
gemeenteselectie = pd.DataFrame({
        'Gemeente': ['Rotterdam', 'Amsterdam', 'Zaanstad', 'Dordrecht', 'Zaltbommel', 'Enkhuizen', 'Hengelo', 'Zoetermeer',
                     'Haarlem', 'Gouda', 'Leusden', 'Groningen'],
        'CBS_code': ['599', '363', '479', '505', '297', '388', '164', '637', '392', '513', '327', '14']})

def read_csv(path):
    df = pd.read_csv(path, sep='\t')
    if len(df.columns)==1:
        df = pd.read_csv(path, sep=';')
    if len(df.columns)==1:
        df = pd.read_csv(path, sep=',')
    return df


def grouphouses(df):
    dfa = df.groupby(['PC6','Buurt2018']).count()[['Huisnummer']]
    dfa = dfa.rename(columns={'Huisnummer':'ca'})
    dfa = dfa.reset_index(level=['Buurt2018','PC6'])
    dfb = df.groupby('PC6').count()[['Huisnummer']]
    dfb = dfb.rename(columns={'Huisnummer':'cb'})
    dfx = pd.merge(dfa, dfb, on='PC6', how='outer')
    dfx['ratio']=dfx.ca/dfx.cb
    return dfx


def selectregion(df,selection):
    if 'POSTCODE_VAN' in df.columns:
        df['POSTCODE_VAN'] = df['POSTCODE_VAN'].str.replace(' ','')
        result = df[df['POSTCODE_VAN'].isin(sleuteltabel['PC6'])]
        return result


def write_df_to_json(df,filename):
    Export = df.to_json(orient='index')
    with open(filename, 'w') as f:
        f.write(Export)


originalsleutel = pd.read_csv(keyfile,delimiter=';')
sleuteltabel = originalsleutel[originalsleutel['Gemeente2018'].isin(gemeenteselectie['CBS_code'])]
sleuteltabel = grouphouses(sleuteltabel)
write_df_to_json(sleuteltabel, '../fastapi/app/data/sleutel.json')

for file in datafiles:
    file_path = '../Data/'+file+'.csv'
    # Read data
    data = selectregion(read_csv(file_path),sleuteltabel)
    # write data as json
    write_df_to_json(data, '../fastapi/app/data/'+file+'.json')
