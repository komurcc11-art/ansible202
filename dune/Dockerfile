#This base image container is awail on hub.docker.com
#it has python3.7 avail on Alpine Linux, a minimalist Linux distribution
FROM python:alpine3.7
COPY . /app
WORKDIR /app
#use python package installer to install the flask library to our image
RUN pip install -r requirements.txt
#container is exposed on port 5000
CMD python ./dune.py
