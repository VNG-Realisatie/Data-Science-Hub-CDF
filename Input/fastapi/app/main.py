''' Dit script is ontwikkeld vanuit de DataScienceHub, onderdeel van VNG-realisatie
als deel van de CommonDataFactory.

Ontwikkelaar: Kees Kraan
'''
# Import libraries
from fastapi import FastAPI
import pandas as pd
import uvicorn
import json
import os
import datetime
import ast
from starlette.requests import Request
from starlette.responses import Response

def write_logging (request, page):
    """ Get the headers of a Request of a specific page:
        Add this method in each API page you have and specify the pagename as a string in the variable 'page'.
        The date + time, pagename and headers of the Request are then added to the logging page. """
    headers = request.headers.items()
    headers = {key:value for (key, value) in headers}
    date_time = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    logdict = {'timestamp':date_time, 'request': page, 'header': headers}
    with open("logging.txt", "a") as myfile:
        print(logdict, file = myfile)


# Define constants
filelocation = 'data/'
files = []
for file in os.listdir(filelocation):
    if file.endswith('.json'):
        files.append(file)

# initiate API
app = FastAPI()

@app.get("/")
async def root(request: Request):
    write_logging(request, 'root')
    return {"Beschikbare data": [value for value in files]}


@app.get("/getdata/{file}")
async def read_item(request: Request, file: str):
    '''Functie waarmee de data uit het geselecteerde bestand teruggegeven wordt. Data wordt aangeleverd als
    python dataframe omgezet naar dictionary met "index" als orient.'''
    write_logging(request, 'getdata ' + file)
    if os.path.isfile(filelocation + file):
        data = pd.read_json(filelocation + file, orient='index')
        return data.to_dict(orient='index')
    else:
        return {'result': 'Bestand niet gevonden'}


@app.get("/test")
def testfunc(request: Request,):
    write_logging(request, 'test')
    return {"value": app.openapi_url}


@app.get("/items/{item_id}")
async def read_item(request: Request, item_id: int, q: str = None):
    write_logging(request, 'items')
    return {"item_id": item_id, "q": q}


@app.get("/logging")
def get_logging():
    with open("logging.txt", "r") as my_file:
        data = my_file.read()
        newdata = {}
        i = 1
        for elem in data.split('\n'):
            if elem != '':
                value = ast.literal_eval(elem)
                newdata[i] = value
                i+=1
    return {"logging": newdata}


# Run API
if __name__ == '__main__':
    uvicorn.run(app, port=4443)




