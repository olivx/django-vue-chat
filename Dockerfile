FROM python:3.7-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apk --no-cache add python build-base python-dev \
    openssl git bash


RUN apk update \
    && apk add --no-cache --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && apk del build-deps \
    && pip install --upgrade pip \ 
    && pip install pipenv 

COPY Pipfile /app/Pipfile
COPY Pipfile.lock /app/Pipfile.lock

RUN pipenv install --system --deploy

COPY . /app/

ENTRYPOINT ["sh", "/app/entrypoint.sh" ]