# Building and deploying a Docker data pipeline

## Requirements
 - Docker

## Configuration

## Getting started

## Building the Docker container
Run `docker build -t datapipeline . --no-cache` to build the container image

## Running the container locally
Run `docker run -dit --env-file .env --name acmepipeline datapipeline`

This will pass in the variable you have set in the .env file and start a named container "acmepipeline" using the image "datapipeline" we built earlier.

If you need to run multiple containers you can give them different names and pass in different configuration files.

Run `docker ps` and look for a running container with the name "acmepipeline"

### Accessing the terminal inside the container to run scripts
 * Run `docker exec -it acmepipeline bash` to connect to a bash terminal inside the docker container.
 * Check to see if your environment variable have loaded by running `env` in the terminal.
 * You can now run the various shell and python scripts to carry out the pipeline tasks.
 * You can run the various workflow scripts directly: 
  * `docker docker exec -it acmepipeline /app/fetch.sh` (Fetch files from sftp pickup point into the incoming directory)
  * `docker docker exec -it acmepipeline /app/decrypt.sh` (Decrypt the files in the incoming directory with PGP key)
  * `docker exec -it acmepipeline /app/publish.py` (no need to run the .sh in docker as no python virtual environment is needed).

### Mounting SSH and PGP keys
TODO: Further detailed instructions.
 * Mount SSH volume, add `-v ~/.ssh:/root/.ssh` to your docker run command.
 * Mount PGP volume, add `-v ~/.gnupg:/root/.gnupg` to your docker run command.

### Setting up cron on the host


## Deploying the Docker container to a server



