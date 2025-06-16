# 🚀 FastAPI Tutorial: Hello API

## Learning How to Run FastAPI Code Locally

Follow these steps to set up and run your FastAPI project on your local machine:

---

### 🛠️ Setup Instructions

1. **Create a virtual environment**
   ```bash
   python -m venv myenv
   ```

2. **Activate the virtual environment**
   ```bash
   myenv\Scripts\activate
   ```

3. **Install required packages**
   ```bash
   pip install uvicorn fastapi
   ```

4. **Run your FastAPI app**
   ```bash
   uvicorn main:app --reload
   ```

---

### 📄 Code Explanation (`main.py`)

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "hello"}

@app.get("/about")
def about():
    return {"message": "Hello I am about page Api"}
```

- **Import FastAPI:** The FastAPI class is imported to create the web app.
- **Create an instance:** `app = FastAPI()` initializes the application.
- **Define endpoints using decorators:**
  - `@app.get("/")`: Listens to requests on the root path `/`.
  - `@app.get("/about")`: Listens to requests on the `/about` path.
- **Return values:**
  - `hello()` returns `{ "message": "hello" }`
  - `about()` returns `{ "message": "Hello I am about page Api" }`

---

### 🔍 Output Preview

- At `http://127.0.0.1:8000/`  
  ```json
  { "message": "hello" }
  ```

- At `http://127.0.0.1:8000/about`  
  ```json
  { "message": "Hello I am about page Api" }
  ```

---

### 📚 Swagger UI for API Testing

Visit this URL in browser to test your API interactively:  
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
