# 🏥 FastAPI Project: Patient Record Management API

A FastAPI project demonstrating **Path Parameters**, **Query Parameters**, and **Exception Handling** using a hospital-style patient record system.

---

## 🚀 Setup & Installation

Follow the steps below to run the FastAPI app locally:

### 🛠️ Environment Setup

1. **Create a virtual environment**

   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment**

   On **Windows**:

   ```bash
   venv\Scripts\activate
   ```

3. **Install required packages**

   ```bash
   pip install fastapi uvicorn
   ```

4. **Run the application**

   ```bash
   uvicorn main:app --reload
   ```

---

## 📂 Project Structure

```
.
├── main.py
└── patients.json
```

- `main.py`: Contains the FastAPI application logic.
- `patients.json`: Sample dataset used for fetching patient records.

---

## 📄 Code Overview (`main.py`)

```python
from fastapi import FastAPI, HTTPException, Path, Query
import json

app = FastAPI()

# Load patient data from a JSON file
def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return {"message": "This is Patient Record Management API"}

@app.get("/view")
def view():
    data = load_data()
    return data

# Get patient record by path parameter
@app.get("/patient/{patient_id}")
def view_patient(patient_id: str):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    return {"error": "Patient Not Found"}

# Get patient record with Path() validation
@app.get("/patients/{patient_id}")
def view_patients(patient_id: str = Path(..., description="ID of the patients in DB", example="P001")):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient Not Found")

# Query parameters for sorting
@app.get("/sort")
def sort_patients(
    sort_by: str = Query(..., description="Sort on the basis of the Height, Weight, BMI"),
    order: str = Query("asc", description="Sort in ascending order or descending order")
):
    valid_fields = ["height", "weight", "bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(status_code=404, detail=f"Invalid fields selected from {valid_fields}")
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid order selected between asc and desc")

    data = load_data()
    sort_order = True if order == "desc" else False
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)
    return sorted_data
```

---


```

---

## 🔍 Output Examples

- `GET /`  
  ```json
  { "message": "This is Patient Record Management API" }
  ```

- `GET /patient/P001`  
  ```json
  {
    "name": "John Doe",
    "age": 30,
    "height": 175,
    "weight": 70,
    "bmi": 22.9
  }
  ```

- `GET /sort?sort_by=bmi&order=desc`  
  Returns patient list sorted by BMI in descending order.

---
