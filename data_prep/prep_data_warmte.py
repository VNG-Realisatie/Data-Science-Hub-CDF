''' Dit script is ontwikkeld vanuit de DataScienceHub, onderdeel van VNG-realisatie
als deel van de CommonDataFactory.

Ontwikkelaar: Kees Kraan
'''
# Import libraries
import pandas as pd
import json

# Define constants
filenames = ['Stedin_Verbruiksdata_2019','Liander_Verbruiksdata_2019']

for file in filenames:
    file_path = 'warmtetransitie/'+file+'.csv'
    # Read data
    df = pd.read_csv(file_path, sep='\t')
    # convert data to json
    Export = df.to_json(orient='index')
    Export = '{"'+file+'":'+Export+'}'
    with open('API/fastapi/app/data/'+file+'.json', 'w') as f:
        f.write(Export)
