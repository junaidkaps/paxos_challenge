############################################################
# Dockerfile to build Paxos Application Container
# Based on Ubuntu
############################################################

# Set the base image to Ubuntu
FROM ubuntu

# File Author / Maintainer
MAINTAINER Junaid Kapadia

# Add the application resources URL - Uncomment if docker throws an error. 
#RUN echo "deb http://archive.ubuntu.com/ubuntu/ $(lsb_release -sc) main universe" >> /etc/apt/sources.list

# Update the sources list
RUN apt-get update

# Install basic applications
RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential

# Install Python and Basic Python Tools
RUN apt-get install -y python python-dev python-distribute python-pip

# Copy the application folder inside the container
ADD paxosChallenge.py  /paxosApp/
ADD requirements.txt /paxosApp/
ADD paxosTornado.py /paxosApp/
ADD key.pem 	   /paxosApp/ 
Add cert.pem      /paxosApp/ 

# Get pip to download and install requirements:
RUN pip install -r /paxosApp/requirements.txt

# Expose ports
EXPOSE 443

# Set the default directory where CMD will execute
WORKDIR /paxosApp

# Start the paxos Program using Flask's production grade Tornado. 
CMD python paxosTornado.py

