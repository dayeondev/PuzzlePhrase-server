FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

WORKDIR /app/
RUN pip install pip==23.3.1
COPY ./requirements.txt /app
RUN pip install -r /app/requirements.txt

COPY ./app /app/app
