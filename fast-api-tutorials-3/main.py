from fastapi import FastAPI, HTTPException, Path, Query
import json

# Initialize the FastAPI app
app = FastAPI()

# Function to load patient data from a local JSON file
def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data

# Root endpoint - simple welcome message
@app.get("/")
def hello():
    return {"message": "This is Patient Record Management API"}

# Endpoint to return the entire patient dataset
@app.get("/view")
def view():
    data = load_data()
    return data

# Endpoint using path parameter to fetch a patient record
@app.get("/patient/{patient_id}")
def view_patient(patient_id: str):
    data = load_data()
    if patient_id in data:
        return data[patient_id]  # Return patient info if ID matches
    return {"error": "Patient Not Found"}  # Return error if not found

# Same functionality as above but with Path() validation metadata
@app.get("/patients/{patient_id}")
def view_patients(
    patient_id: str = Path(..., description="ID of the patients in DB", example="P001")
):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    # Raises an HTTP 404 error if patient is not found
    raise HTTPException(status_code=404, detail="Patient Not Found")

# Endpoint to sort patients using query parameters (height, weight, bmi)
@app.get("/sort")
def sort_patients(
    sort_by: str = Query(..., description="Sort on the basis of the Height, Weight, BMI"),
    order: str = Query("asc", description="Sort in ascending order or descending order")
):
    # Allowed fields to sort on
    valid_fields = ["height", "weight", "bmi"]

    # Validate sort field
    if sort_by not in valid_fields:
        raise HTTPException(status_code=404, detail=f"Invalid fields selected from {valid_fields}")
    
    # Validate order
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid order selected between asc and desc")

    # Load and sort data
    data = load_data()
    sort_order = True if order == "desc" else False  # Determine sorting order
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data  # Return sorted list
