#!/bin/bash
set -eu

export ARCHIVE_DIR=/var/lib/ckan_data_pipeline/archive/
export FILES_TO_PUBLISH_DIR=/var/lib/ckan_data_pipeline/incoming/

mkdir -p $ARCHIVE_DIR
mkdir -p $FILES_TO_PUBLISH_DIR

if [ -z "$CKAN_URL" ]; then
    exit 1
fi

if [ -z "$CKAN_API_KEY" ]; then
    exit 1
fi

if [ -z "$CKAN_CLIENT_USER_AGENT" ]; then
    exit 1
fi

if [ -z "$CKAN_PACKAGE_ID" ]; then
    exit 1
fi

if [ -z "$SSH_KEY_FILE" ]; then
    exit 1
fi

if [ -z "$SFTP_USER" ]; then
    exit 1
fi

if [ -z "$SFTP_HOST" ]; then
    exit 1
fi

if [ -z "$SFTP_DIR" ]; then
    exit 1
fi

if [ ! -f "$DECRYPTION_KEY" ]; then
    echo "Fetching and publishing data"
    ./fetch.sh && python publish.py
    exit 0
fi

echo "Import the private key for decrypting data"
gpg --import "$DECRYPTION_KEY"

echo "Fetching, decrypting and publishing data"
./fetch.sh && ./decrypt.sh && python publish.py