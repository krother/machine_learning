# Use an official Python runtime as a parent image
FROM python:3.8-slim

WORKDIR /course

COPY requirements.txt /course

# Install any needed packages specified in requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run app.py when the container launches
CMD ["jupyter", "notebook", "--allow-root", "--ip=0.0.0.0"]