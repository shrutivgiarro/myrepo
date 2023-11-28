# FROM python:3
# ENV PYTHONUNBUFFERED=1
# WORKDIR /code
# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt
# COPY . .
# EXPOSE 8000
# CMD ["python","manage.py","runserver"]

# FROM python:3

# # USER app
# ENV PYTHONUNBUFFERED 1
# # RUN mkdir /db
# # RUN chown app:app -R /db

# RUN mkdir /code
# WORKDIR /code
# ADD requirements.txt /code/
# RUN pip install -r requirements.txt
# ADD . /code/

FROM python:3.11.4-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY . /app/

RUN apt-get update

COPY ./requirements.txt .
RUN pip install -r requirements.txt