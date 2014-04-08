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
RUN apt-get -y install python-pip xvfb libfreetype6 libfontconfig wget

#get phantomjs libraries
RUN apt-get -y install libkrb5-3 libk5crypto3 libqt4-declarative liblcms1 libjpeg-turbo8 libjpeg8 iso-codes qdbus ttf-dejavu-core libqt4-script libqt4-network libqt4-dbus libgnutls26 xml-core libtasn1-3 libmysqlclient18 libqt4-xmlpatterns fontconfig libavahi-common-data libp11-kit0 libcups2 libqtcore4 libkrb5support0 fontconfig-config libxml2 libkeyutils1 libqt4-sql libxrender1 liborc-0.4-0 sgml-base libqt4-xml libtiff4 libgstreamer-plugins-base0.10-0 libqtgui4 libavahi-client3 krb5-locales libfontconfig1 libqt4-sql-mysql libgssapi-krb5-2 libxi6 libqtwebkit4 libgstreamer0.10-0 libaudio2 libavahi-common3 mysql-common libmng1

#download phantomjs
RUN wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.7-linux-x86_64.tar.bz2 --no-check-certificate

# untar and remove tar
RUN tar -xvf phantomjs-1.9.7-linux-x86_64.tar.bz2 && rm phantomjs-1.9.7-linux-x86_64.tar.bz2

RUN mv phantomjs-1.9.7-linux-x86_64 /usr/local/.

RUN ln -s /usr/local/phantomjs-1.9.7-linux-x86_64/bin/phantomjs /usr/local/bin/.

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
 
