# path_query_params
from fastapi import FastAPI, HTTPException, Path, Query
import json

app = FastAPI()

# A function created to load the dataset
def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)

    return data

@app.get('/')
def hello():
    return {'message':'This is Patient Record Management API'}


def about():
    return {'message':'A fully Functional Project API to manage the Hospital Patient Records'}

@app.get('/view')
def view():
    data = load_data()

    return data

# Path Params
@app.get('/patient/{patient_id}')
def view_patient(patient_id : str):
    # Load all the patients
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    return {'error': 'Patient Not Found'}

# Same path parameters but with Path Functions(Title, Description etc)
@app.get('/patients/{patient_id}')
def view_patients(patient_id : str = Path(... , description = 'ID of the patients in DB', example = 'P001')):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='Patient Not Found') # uSED httpeXCEPTION AT THE Place of Error

# Query Params
@app.get('/sort')
def sort_patients(sort_by: str = Query(...,description = 'Sort on the basis of the Height, Weight, BMI'), order: str = Query('asc',description = 'Sort in ascending order or descending order')):

    valid_fields = ['height','weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code = 404, detail= f'Invalid fields selected from {valid_fields}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail= f'Invalid order selected between asc and desc')
    
    data = load_data()

    sort_order = True if order == 'desc' else False

    sorted_data = sorted(data.values(), key= lambda x: x.get(sort_by, 0), reverse = False)