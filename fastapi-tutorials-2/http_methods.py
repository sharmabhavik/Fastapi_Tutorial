from fastapi import FastAPI
import json

# Initialize FastAPI app
app = FastAPI()

# Function to load patient data from a JSON file
def data_load():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data

# Root endpoint - returns a basic welcome message
@app.get("/")
def hello():
    return {'message': 'Patient Management System'}

# About endpoint - describes the purpose of the API
@app.get('/about')
def about():
    return {'message': 'A fully functional Project API to manage Hospital Patient Records'}

# View endpoint - returns all patient records from the JSON file
@app.get('/view')
def view():
    data = data_load()
    return data
