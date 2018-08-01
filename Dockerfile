FROM python:2.7-slim
COPY . /app
WORKDIR /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN apt-get update; apt-get install ssh-client wget -y
