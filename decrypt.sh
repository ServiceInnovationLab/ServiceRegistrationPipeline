#!/bin/bash
if [ -f .env ]; then
    source .env
fi

set -eu

FILES=$FILES_TO_PUBLISH_DIR*.gpg

for f in $FILES
do
  echo "Processing $f file..."
  output_file=${f%.*}
  echo $output_file " decrypted"

  #decrypt the files
  gpg --output $output_file --decrypt $f

  #clean up
  rm $f

done
