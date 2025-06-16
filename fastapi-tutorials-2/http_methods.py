from fastapi import FastAPI
import json

app = FastAPI()

# A function created to load the dataset
def data_load():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    
    return data

@app.get("/")
def hello():
    return {'message':'Patient Management System'}

@app.get('/about')
def about():
    return {'message':'A fully functional Project API to manage Hospital Patient Records'}

@app.get('/view')
def view():
    data = data_load()

    return data
