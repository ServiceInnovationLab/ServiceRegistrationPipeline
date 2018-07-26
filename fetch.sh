#!/bin/bash
source .env
set -euv

sftp -i $SSH_KEY_FILE $SFTP_USER@$SFTP_HOST:$SFTP_DIR/*.* ./incoming/
