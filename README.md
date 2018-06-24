# ServiceRegistrationPipeline

Takes existing data on NZ Government services, and publishes on CKAN (data.govt.nz) in reasonable formats

1) Get an publisher api key from data.govt.nz, place in `.env` (see env-example file)
2) add cron job


# Sample cron job
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

# Work flow

Here's what it does:

First, it fetches the data (from MSD). (see fetch.sh)

Then it decrypts the data we got from MSD (see decrypt.sh)

Then it publishes this data on data.govt.nz (see publish.sh)

# Fetching

MSD place the data on their SFTP server. Configure your credentials in `.env`.

* `FILES_TO_PUBLISH_DIR`: Directory to place fetched files in
* `SFTP_HOST`: the host to connect to
* `SFTP_USER`: the user to connect as
* `SFTP_DIR`: the folder to look in on the sftp server

# Decryption

MSD encrypt this data. They use PGP keys. We've supplied them the public key and they use this to encrypt before sending to us. Configure your user's gpg appropriately

* `ARCHIVE_DIR`: The directory to place decrypted files

# Publishing

Data.govt.nz allows publishing with an API key. Configure your credentials in `.env`

* `CKAN_API_KEY`: Your ckan api key
* `CKAN_CLIENT_USER_AGENT`: Make up a ckan client user agent
* `CKAN_URL`: Which CKan are you talking to
* `CKAN_PACKAGE_ID`: Package you're publishing to

* `FILES_TO_PUBLISH_DIR`: Dir as used in fetch.sh and decrypt.sh
* `ARCHIVE_DIR`: Dir as used in fetch.sh and decrypt.sh
