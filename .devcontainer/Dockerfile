# Identify the base container image
FROM python

# Setup the image dependencies
RUN apt-get update -y
RUN useradd -m -s /bin/bash mcdaniel
RUN apt-get install -y python3-pip less
RUN pip3 install numpy pandas matplotlib seaborn

# Setup the directory to use for build
USER mcdaniel
WORKDIR /home/mcdaniel

