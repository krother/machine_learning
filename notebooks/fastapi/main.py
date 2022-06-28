"""
Hello World example from https://fastapi.tiangolo.com/

start with:

    pip install "uvicorn[standard]"
    uvicorn main:app --reload

API at:
  
    http://127.0.0.1:8000/

Swagger at:

    http://127.0.0.1:8000/docs

"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/fruit/{color}/{size}")
def fruit_predictor(color: str, size: int):
    if color == 'green':
        if size < 5:
            result = 'apple'
        else:
            result = 'watermelon'
    elif color == 'yellow':
        result = 'banana'
    elif color == 'orange':
        result = 'an orange of course'

    return {
        "result": result,
        "color": color,
        "size": size
        }