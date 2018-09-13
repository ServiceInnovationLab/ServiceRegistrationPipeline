FROM python:2.7-slim
COPY . /app
WORKDIR /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN apt-get update; apt-get install ssh-client wget gpg -y --no-install-recommends && rm -rf /var/lib/apt/lists*
VOLUME ["/incoming", "/archive"]
CMD ["/app/docker-cmd.sh"]