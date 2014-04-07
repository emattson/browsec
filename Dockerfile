#################################################
# Dockerfile to build bastion container images
# Based on Ubuntu
##################################################

# set the base image to ubuntu
FROM ubuntu

#get TERM
RUN echo $TERM

#set TERM?
RUN export TERM='xterm'

# update apt
RUN apt-get -y update

RUN apt-get -y install dialog
# get phantomjs and pip
RUN apt-get -y install phantomjs python-pip

# get selenium 
RUN pip install -v selenium 

# get flask
RUN pip install -v flask

# get virtualdisplay
RUN pip install -v pyvirtualdisplay

# done with dependencies
RUN echo done installing dependencies!

# make source directory
RUN mkdir /src

# bundle app source
ADD web-server /src

# expose port
EXPOSE 8887

# set working dir
WORKDIR /src/

# start web server
CMD ["python", "webserver_bastion.py"]
 
