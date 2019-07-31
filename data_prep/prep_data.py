''' Dit script is ontwikkeld vanuit de DataScienceHub, onderdeel van VNG-realisatie
als deel van de CommonDataFactory.

Ontwikkelaar: Kees Kraan
'''
# Import libraries
import pandas as pd
import json

# Define constants
filename = 'Energie_small'
file_path = filename+'.xlsx'

# Read excel
df = pd.read_excel(file_path, encoding='utf-16')
# set index to names of gemeenten
df = df.set_index('Gemeente')
# convert exceldata to json
Export = df.to_json(orient='index')
Export = '{"'+filename+'":'+Export+'}'
with open('fastapi/app/'+filename+'.json', 'w') as f:
    f.write(Export)
# {filename+'.xlsx': Export}
