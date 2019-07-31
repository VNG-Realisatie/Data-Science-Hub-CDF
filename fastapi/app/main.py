''' Dit script is ontwikkeld vanuit de DataScienceHub, onderdeel van VNG-realisatie
als deel van de CommonDataFactory.

Ontwikkelaar: Kees Kraan
'''
# Import libraries
from fastapi import FastAPI
import uvicorn
import json
import os

# Define constants
test = True
filelocation = 'data/'

if test == True:
    first = True
    for file in os.listdir(filelocation):
        if file.endswith('.json'):
            if first == True:
                with open(filelocation+file, 'r') as infile:
                    totaldata = json.load(infile)
                first = False
            else:
                with open(filelocation+file, 'r') as infile:
                    file_data = json.load(infile)
                    for key, item in file_data.items():
                        totaldata[key] = (item)
else:
    filename = 'Energie_small'
    # Load jsonfile
    with open(filename+'.json', 'r') as f:
        data = json.load(f)

for key, item in totaldata.items():
    print(key,len(totaldata[key]))

# initiate API
app = FastAPI()


@app.get("/")
async def root():
    return {"Beschikbare data": [key for key, value in totaldata.items()]}


@app.get("/test")
def testfunc():
    return {"value": app.openapi_url}


@app.get("/file/{file_name}")
async def return_filedata(file_name: str):
    return {"Beschikbare data": [key for key, value in data[file_name].items()]}


@app.get("/file/{file_name}/{columns}")
async def return_columns(file_name: str, columns: str):
    print('check', columns)
    if columns.find(',')>0:
        columns = columns.split(',')
    elif columns == 'all':
        return {"file_name": data[file_name]}
    else:
        columns = [columns]
    print(columns)
    return {file_name: [data[file_name].get(key) for key in columns]}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

# Run API
if __name__ == '__main__':
    uvicorn.run(app, port=4443)
