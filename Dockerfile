#################################################
# Dockerfile to build bastion container images
# Based on Ubuntu
##################################################

#set the base image to ubuntu
FROM ubuntu

#update apt
RUN apt-get -y update

RUN apt-get -y install dialog
#get phantomjs and pip
RUN apt-get -y install phantomjs python-pip

#get selenium 
RUN pip install -v selenium 

#get flask
RUN pip install -v flask

#get virtualdisplay
RUN pip install -v pyvirtualdisplay

# done with dependencies
RUN echo done installing dependencies!

#make source directory
RUN mkdir /src

#bundle app source
ADD web-server /src

#check
 
