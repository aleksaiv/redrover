FROM python:3.12-alpine

WORKDIR /usr/workspace
COPY ./requirements.txt /usr/workspace
RUN pip3 install -r requirements.txt
