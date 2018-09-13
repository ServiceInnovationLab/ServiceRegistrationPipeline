#!/bin/bash
if [ -f .env ]; then
    source .env
fi
set -euv

sftp -i $SSH_KEY_FILE $SFTP_USER@$SFTP_HOST:$SFTP_DIR/*.* $FILES_TO_PUBLISH_DIR
