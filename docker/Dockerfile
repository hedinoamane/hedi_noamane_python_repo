# Use the official image as a parent image.
# Set base image (host OS)
# Grab the latest alpine image
FROM alpine:latest
# FROM ubuntu:20.04
# FROM python:3.8

# Install python and pip
RUN apk add --no-cache --update python3 py3-pip bash
ADD app/requirements.txt /tmp/requirements.txt

# Install dependencies
RUN pip3 install --no-cache-dir -q -r /tmp/requirements.txt
# RUN apt-get -qq update -y \
#  && apt-get -qq install -y python3-pip python3-dev \
#  && cd /usr/local/bin \
#  && ln -s /usr/bin/python3 python \
#  && pip3 install --upgrade pip

# Add our code
ADD app /opt/app/
WORKDIR /opt/app

# Expose is NOT supported by Heroku
EXPOSE 5000

# Run the image as a non-root user
RUN adduser -D ZAakdazd
USER ZAakdazd

# ENTRYPOINT ["python", "app/app.py"]
# CMD [ "python", "./app/app.py" ]

# Run the app.  CMD is required to run on Heroku
# define ENV PORT for localhost
# ENV PORT 5000
# $PORT is set by Heroku
CMD gunicorn --bind 0.0.0.0:$PORT wsgi

