FROM python:3.10-alpine


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY pets_api/ .
COPY requirements.txt .

RUN pip install -r requirements.txt
