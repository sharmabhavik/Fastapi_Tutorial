# 🏥 FastAPI Project: Patient Record API using HTTP Methods

This project is a beginner-friendly FastAPI application to demonstrate how to use **HTTP methods** (like `GET`) to build an API that manages hospital patient data stored in a JSON file.

---

## 📌 What are HTTP Methods?

- `GET` → Fetch data from the server (used in this project)
- `POST` → Send new data to the server (e.g., add a new patient)
- `PUT` → Update existing data on the server
- `DELETE` → Remove data from the server

> 🧠 In this project, we focus on **GET** methods only — to retrieve patient information.

---

## 🚀 How to Run Locally

### 🛠️ Setup Instructions

1. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment**

   On **Windows**:
   ```bash
   venv\Scripts\activate
   ```

3. **Install FastAPI and Uvicorn**
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
├── http_methods.py     # Main FastAPI app
└── patients.json         # Patient data in JSON format
```

---

## 📄 Code Overview (`http_methodspy.py`)

```python
from fastapi import FastAPI
import json

# Initialize FastAPI app
app = FastAPI()

# Function to load patient data from a JSON file
def data_load():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data

# Root endpoint - GET method
@app.get("/")
def hello():
    return {'message': 'Patient Management System'}

# About endpoint - GET method
@app.get('/about')
def about():
    return {'message': 'A fully functional Project API to manage Hospital Patient Records'}

# View endpoint - GET method to fetch all patients
@app.get('/view')
def view():
    data = data_load()
    return data
```

---

## 📬 Available GET Endpoints

| Route         | Description                                  |
|---------------|----------------------------------------------|
| `/`           | Returns welcome message                      |
| `/about`      | Returns short API description                |
| `/view`       | Returns all patient records from JSON        |

---

## 🔍 Output Examples

- **GET /**  
  ```json
  {
    "message": "Patient Management System"
  }
  ```

- **GET /about**  
  ```json
  {
    "message": "A fully functional Project API to manage Hospital Patient Records"
  }
  ```

- **GET /view**  
  Returns all records like:
  ```json
  {
    "P001": {
      "name": "John Doe",
      "age": 30,
      "height": 175,
      "weight": 70,
      "bmi": 22.9
    },
    ...
  }
  ```

---
