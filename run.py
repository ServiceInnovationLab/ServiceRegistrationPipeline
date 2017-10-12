#!/usr/bin/env python3.5
from os import listdir
from os.path import isfile, join
import os
from dotenv import load_dotenv, find_dotenv
from ckanapi import RemoteCKAN
import ServiceRegistrationPipeline

print(find_dotenv())

# Load config from .env
load_dotenv(find_dotenv())

CKAN_API_KEY = os.environ.get('CKAN_API_KEY')
CKAN_CLIENT_USER_AGENT = os.environ.get('CKAN_CLIENT_USER_AGENT')
CKAN_URL = os.environ.get('CKAN_URL')
CKAN_PACKAGE_ID = os.environ.get('CKAN_PACKAGE_ID')

FILES_TO_PUBLISH_DIR = os.environ.get('FILES_TO_PUBLISH_DIR')
ARCHIVE_DIR = os.environ.get('ARCHIVE_DIR')

DATA_GOVT_NZ = RemoteCKAN(CKAN_URL, apikey=CKAN_API_KEY,
                          user_agent=CKAN_CLIENT_USER_AGENT)

def publish_fsd():
    files = ServiceRegistrationPipeline.find_files(FILES_TO_PUBLISH_DIR)

    for filename in files:
        file_to_publish = "{dir}{filename}".format(
            dir=FILES_TO_PUBLISH_DIR, filename=filename)
        print(file_to_publish)

        # Publish
        DATA_GOVT_NZ.action.resource_create(
            package_id=CKAN_PACKAGE_ID,
            url='dummy-value',  # ignored but required by CKAN<2.6
            upload=open(file_to_publish, 'rb'))

        # Archive
        archive_filename = "{dir}{filename}".format(
            dir=ARCHIVE_DIR, filename=filename)
        os.rename(file_to_publish, archive_filename)


def delete_existing_resources():
    package = DATA_GOVT_NZ.action.package_show(id=CKAN_PACKAGE_ID)
    resources = package.get('resources')
    for r in resources:
        resource_id = r.get('id')
        DATA_GOVT_NZ.action.resource_delete(id=resource_id)

if __name__ == "__main__":
    publish_fsd()
