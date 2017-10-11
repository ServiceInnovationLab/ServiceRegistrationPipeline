#!/usr/bin/env python3.5
from os import listdir
from os.path import isfile, join
import os
from dotenv import load_dotenv, find_dotenv
from ckanapi import RemoteCKAN

print(find_dotenv())

# Load config from .env
load_dotenv(find_dotenv())

CKAN_API_KEY = os.environ.get('CKAN_API_KEY')
CKAN_CLIENT_USER_AGENT = os.environ.get('CKAN_CLIENT_USER_AGENT')
CKAN_URL = os.environ.get('CKAN_URL')
CKAN_PACKAGE_ID = os.environ.get('CKAN_PACKAGE_ID')

FILES_TO_PUBLISH_DIR = os.environ.get('FILES_TO_PUBLISH_DIR')
ARCHIVE_DIR = os.environ.get('ARCHIVE_DIR')


if __name__ == "__main__":
    print(CKAN_URL)
    files = [f for f in listdir(FILES_TO_PUBLISH_DIR) if isfile(join(FILES_TO_PUBLISH_DIR, f))]
    mysite = RemoteCKAN(CKAN_URL, apikey=CKAN_API_KEY,
                        user_agent=CKAN_CLIENT_USER_AGENT)
    for f in files:
        filename = "{dir}{file}".format(dir=FILES_TO_PUBLISH_DIR, file=f)
        print(filename)
        mysite.action.resource_create(
            package_id=CKAN_PACKAGE_ID,
            url='dummy-value',  # ignored but required by CKAN<2.6
            upload=open(filename, 'rb'))

