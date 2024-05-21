# Identify the base container image
FROM python:3.9

# Setup the image dependencies
RUN apt-get update -y
RUN useradd -ms /bin/bash mcdaniel
RUN apt-get install -y python3-pip
RUN pip install numpy pandas

# Setup the directory to use for build
USER mcdaniel
WORKDIR /home/mcdaniel

