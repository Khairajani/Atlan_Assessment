# pull official base image: python3.6-buster
FROM python:3.6-buster

# set work directory
WORKDIR /usr/src/app

RUN apt-get update && apt-get install python3-pip -y
RUN apt-get install -y libsm6 libxext6 libxrender-dev netcat

# install dependencies
RUN pip install -U pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install gunicorn==20.0.4
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/

EXPOSE 7001