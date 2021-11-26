FROM python:latest
WORKDIR /application
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./app/ .
EXPOSE 8000
CMD ['uvicorn', 'main:app', '--reload']
