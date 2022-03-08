# FROM ubuntu:18.04

# RUN apt update -y  &&  apt upgrade -y && apt-get update 
# RUN apt install -y curl python3.7 git python3-pip openjdk-8-jdk unixodbc-dev

# # Add SQL Server ODBC Driver 17 for Ubuntu 18.04
# RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
# RUN curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
# RUN apt-get update
# RUN ACCEPT_EULA=Y apt-get install -y --allow-unauthenticated msodbcsql17
# RUN ACCEPT_EULA=Y apt-get install -y --allow-unauthenticated mssql-tools
# RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile
# RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc

# WORKDIR /code
# COPY requirements.txt /code/
# RUN pip3 install -r requirements.txt
# COPY . /code/

# RUN python manage.py runserver


# FROM python:3.8.5-alpine

# COPY . /app
# WORKDIR /app

# RUN apk add --no-cache mariadb-connector-c-dev
# RUN apk update && apk add python3 python3-dev mariadb-dev build-base && pip3 install mysqlclient && apk del python3-dev mariadb-dev build-base

# RUN apk add netcat-openbsd

# RUN pip install -r requirements.txt


FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /my_app_dir
WORKDIR /my_app_dir
ADD requirements.txt /my_app_dir/
RUN pip install — upgrade pip && pip install -r requirements.txt
ADD . /my_app_dir/