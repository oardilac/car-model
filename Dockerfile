# Use an official lightweight Python image.
# https://hub.docker.com/_/python
#FROM python:3.7-slim
FROM python:3.9-buster

ENV PYTHONUNBUFFERED True

# Copy local code to the container image.
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py /app/
COPY modelFirst.pkl /app/
COPY modelSecond.pkl /app/
COPY scaler.pkl /app/
COPY templates /app/templates
COPY static /app/static


    # Service must listen to $PORT environment variable.
    # This default value facilitates local development.
ENV PORT 8080

    # Run the web service on container startup. Here we use the gunicorn
    # webserver, with one worker process and 8 threads.
    # For environments with multiple CPU cores, increase the number of workers
    # to be equal to the cores available.
CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 app:app