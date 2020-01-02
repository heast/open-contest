#!/bin/bash

apt-get update

# Install dependencies
apt-get -y install nodejs npm python3.8-dev python3-pip docker.io psmisc nginx
npm install -g nodemon

# Create a system user for the contest system
#addgroup contest
#adduser --group contest contest
