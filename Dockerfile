# base image
FROM python:3.11

#directory to store app source code
RUN mkdir /authflow

#switch to /app directory so that everything runs from here
WORKDIR /authflow

COPY requirements.txt ./
RUN pip install django
RUN pip install -r requirements.txt

#copy the app code to image working directory
COPY ./authflow /authflow