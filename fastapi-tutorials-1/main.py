# My First Fastapi hello code
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {'message':'hello'}

@app.get("/about")
def about():
    return {'message':'Hello I am about page Api'}