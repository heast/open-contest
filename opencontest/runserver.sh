#!/bin/bash

/usr/sbin/nginx
echo "ran nginx command"
#uwsgi --http :8001 --module opencontest.wsgi
uwsgi --threads 10 --socket 0.0.0.0:8001 --module opencontest.wsgi
echo "ran uwsgi command"
