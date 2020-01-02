ARG USER=heast
# ARG OC_PROJECT_NAME=open-contest-django
ARG OC_PROJECT_NAME=oc-test
ARG PROJECT_PATH=~/open-contest/opencontest

# Include all the mini-dockerfiles used for contest submissions in this build.
FROM $USER/$OC_PROJECT_NAME-c-runner
FROM $USER/$OC_PROJECT_NAME-cpp-runner
FROM $USER/$OC_PROJECT_NAME-cs-runner
FROM $USER/$OC_PROJECT_NAME-java-runner
FROM $USER/$OC_PROJECT_NAME-python3-runner
FROM $USER/$OC_PROJECT_NAME-ruby-runner
FROM $USER/$OC_PROJECT_NAME-vb-runner

FROM ubuntu:bionic

# Install dependencies.
COPY setup.sh /setup.sh
RUN ./setup.sh
# RUN apt-get update && \
#     apt-get -y install nodejs npm python3 python3-pip docker.io psmisc nginx
# RUN npm install -g nodemon
# RUN addgroup --system contest && adduser --system --group contest contest
# RUN pip3 install markdown2 uwsgi readerwriterlock
ADD requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt

# Symlink the nginx config so that nginx can find it.
RUN ln -s $PROJECT_PATH/nginx.conf /etc/nginx/sites-enabled/
# RUN ln -s -f /usr/bin/python3 /usr/bin/python

# Tell docker to allow nginx access to the following ports:
# nginx's natural habitat
#EXPOSE 80
## uwsgi listens on 8001, users access on 8000.
#EXPOSE 8000
#EXPOSE 8001

COPY . $PROJECT_PATH/
COPY uwsgi_params /uwsgi_params
COPY runserver.sh /runserver.sh

# original
#ENTRYPOINT [ "uwsgi", "--threads", "10", "--http", "0.0.0.0:8000", "--static-map", "/static=/code/serve", "--module", "code", "--log-5xx", "--disable-logging" ]
#CMD ["nginx"]
ENTRYPOINT ["uwsgi", "--threads", "10", "--http", "0.0.0.0:8000", "--module", "opencontest.wsgi"]

# Use the following run command:
# sudo docker run -p 8000:8000 oc-test:2
