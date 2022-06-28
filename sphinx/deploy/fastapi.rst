
FastAPI
=======

**FastAPI is a very lightweight web server built on top of Flask that makes creating JSON APIs easy.**

FastAPI can be used to expose model predictions and data pipelines to other machines.

Installation
------------

::

    pip install fastapi
    pip install "uvicorn[standard]"
   
`uvicorn` is a HTTP proxy server. In production you might already have a different one.


Example Application
-------------------

The code below defines a simple end-to-end example with FastAPI.


.. code:: python3

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

*The code was adapted from the `Hello World example on FastAPI <https://fastapi.tiangolo.com/>`__ .*

Starting the Server
-------------------

Save the code in a file `main.py`. Go to the directory and type:

:: 

    uvicorn main:app --reload

You find the API in your browser at `http://127.0.0.1:8000/ <http://127.0.0.1:8000/>`__

For the second API function, try accessing `http://127.0.0.1:8000/fruit/yellow/2 <http://127.0.0.1:8000/fruit/yellow/2>`__


Documentation
-------------

The API is self-documenting, created by **Swagger**. See the docs on:

::

    http://127.0.0.1:8000/docs




.. container:: banner reading

   Further Reading

.. highlights::

   `FastAPI Homepage fastapi.tiangolo.com <https://fastapi.tiangolo.com/>`__
