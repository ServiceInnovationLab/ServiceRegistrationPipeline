#!/bin/bash
source .env
set -eu


FILES=$FILES_TO_PUBLISH_DIR/*.gpg

for f in $FILES
do
  echo "Processing $f file..."
  bn=$(basename $f)
  # take action on each file. $f store current file name
  encrypted_file="$FILES_TO_PUBLISH_DIR$bn"
  output_file=${encrypted_file%.*}
  echo $output_file
  gpg --output $output_file --decrypt $f && mv -f $f $ARCHIVE_DIR
done
