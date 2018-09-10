# Data pipeline documentation

## Installation
 1. Setup your servers operating system, dependancies and crypto (ssh/gpg keys).
 2. `git clone` this repository and `cd` into the directory. 
 3. `pyenv install` will install the correct python version.
 4. `virtualenv ./venv` install the python virtual environment.
 5. `source .venv/bin/activate && pip install -r requirements.txt` to install the requirements into the `virtualenv` when done you can `deactivate`. 
 6. `cp env-example .env` then update with the credentials (see documentation below).
 7. Add cron job (see documentation below for an example).

 ## Generating an SSH key
 - Run `ssh-keygen -t rsa` to generate a private/public key pair.
 - Get a copy of the public key at `~/.ssh/id_rsa.pub` to place in the data pickup point server's `authorized_keys` file to allow you access.

## Generating a GPG key
 - Run `gpg --expert --gen-key` and fill in the credentials (use a 4096bit key as a preference).
 - Export your public key to be used to encrypt data you will later fetch using `gpg -a --export NAME_OF_USER_HERE > public_key.gpg`.

## API Key
Get your API key from your user profile in CKAN, place in `.env` (see env-example file)

## Fetching

Configure your credentials in `.env`.

* `FILES_TO_PUBLISH_DIR`: Directory to place fetched files in.
* `SFTP_HOST`: the host to connect to.
* `SFTP_USER`: the user to connect as.
* `SFTP_DIR`: the folder to look in on the sftp server.

## Decryption

Uses PGP/GPG keys. You should provide your public key to the data provider and they should encrypt before moving to their sftp pickup point. Configure your user's gpg appropriately.

* `ARCHIVE_DIR`: The directory to place decrypted files.

## Publishing

Publishing on CKAN requires an API key. Configure your credentials in `.env`

* `CKAN_API_KEY`: Your ckan api key (the user will need write permissions on the dataset you're pushing data to).
* `CKAN_CLIENT_USER_AGENT`: Make up a ckan client user agent.
* `CKAN_URL`: Which CKan are you talking to.
* `CKAN_PACKAGE_ID`: Package you're publishing to.
* `FILES_TO_PUBLISH_DIR`: Dir as used in fetch.sh and decrypt.sh.
* `ARCHIVE_DIR`: Dir as used in fetch.sh and decrypt.sh.

## Sample cron job
```
13 06 * * * $HOME/cronjob.sh
```

sample cronjob.sh
```
#!/bin/bash

# Redirect output to syslog
exec 1> >(logger -s -t $(basename $0)) 2>&1

cd /home/regpipeline/ServiceRegistrationPipeline

./fetch.sh && ./decrypt.sh && ./publish.sh

```
