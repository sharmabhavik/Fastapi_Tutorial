# 🏥 FastAPI Project: Basic Patient Record API

This project implements a simple hospital-style **Patient Management API** using FastAPI. It reads data from a local JSON file and provides basic routes to access patient information.

---

## 🚀 How to Run Locally

Follow these steps to get started with the FastAPI app:

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
├── http_methods.py           # FastAPI app
└── patients.json     # Sample patient data
```

---

## 📄 Code (`main.py`)

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
```

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
  Returns all patient records from `patients.json` in JSON format.

---
