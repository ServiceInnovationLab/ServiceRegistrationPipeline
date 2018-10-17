# Building and deploying a Docker data pipeline

## Requirements
 - Docker

## Configuration

Docker requires a few additional configuration keys to work. See the docker-env-example file. The easiest way to manage configuration is by putting them in a file and setting them using the `--env-file` flag in your docker run command

| Key                    | purpose                                                                        |
|------------------------|:------------------------------------------------------------------------------:|
| CKAN_API_KEY           | your ckan API access key                                                       |
| CKAN_URL               | The url of the ckan instance                                                   |
| CKAN_CLIENT_USER_AGENT | a user agent string so you can identify the api calls                          |
| CKAN_PACKAGE_ID        | the id/slug of the dataset you will update with resources                      |
| SSH_KEY_FILE           | You will need to mount a ssh key for sftp access, this is the path of that key |
| SFTP_HOST              | the host of the sftp server                                                    |
| SFTP_USER              | the username for access to the sftp server                                     |
| SFTP_DIR               | the directory of the sftp server that will be accessed                         |
| DECRYPTION_KEY         | The path of the GPG key which has been mounted into the container              |

## Getting started

## Building the Docker container
Run `docker build -t datapipeline . --no-cache` to build the container image

## Running the container locally


```
docker run -it --env-file ckan_data_pipeline.env \
 -v archive:/archive \
 -v ~/.ssh/id_rsa:/id_rsa \
 -v ~/Code/dia/decrypt_secret.asc:/decrypt_secret.asc \
 --name fsd datapipeline bash
```

## Deploying the Docker container to a server


### Pushing a new version of the code to the server
TODO

### Deploying the container on a server
TODO

### Running as a cron

TODO


