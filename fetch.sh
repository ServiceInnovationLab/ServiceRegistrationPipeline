#!/bin/bash
source .env
set -euv

ssh-add $SSH_KEY_FILE
sftp $SFTP_USER@$SFTP_HOST:$SFTP_DIR/* ./incoming/

gpg --decrypt incoming/*
