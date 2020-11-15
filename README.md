# TracerIND

TracerIND is CITF's own Medical History analysis and tracking tool. Based on a Django DRF - ReactJS - Nginx Configuration

## Installation

Setup of backend requires Python version 3+ and PostgreSQL
Follow Instructions below to install and migrate:

```bash
$ sudo apt-get update
$ sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib 
```
Now,to clone code, make Virtual env and setup the database and Django Framework:

```bash
$ sudo apt-get install virtualenv
$ mkdir ~/TracerIND && cd TracerIND
$ virtualenv venv
# now activate virtual env
$ source venv/bin/activate
# install requirements
$ pip3 install django djangorestframework djangorestframework-jwt django-cors-headers psycopg2-binary django-allauth
# download database backup from link : https://drive.google.com/drive/folders/1AbTPsgRXrRmd87vDNapyHwv-QM8QYr2I?usp=sharing
# to restore backup and set database
$ sudo -u postgres psql
$ CREATE DATABASE tracerind;
$ \password
$ admin1234
$ \q

# now restore
$ sudo -u postgres psql tracerind < /Resources/tracerdatabak.sql
$ cd <path to TracerIND>
# start virtual env
$ cd TracerIND
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py runserver

Localhost:8000/api => API local endpoint
```
