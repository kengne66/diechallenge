FROM amazonlinux:latest
MAINTAINER Pierre Kengne 

# Date: 004-104-12-204-12-2021

RUN yum update
#RUN yum install python3.7
RUN mkdir /opt/challenge/

COPY * /opt/challenge/
CMD /bin/bash
RUN cd /opt/challenge/


