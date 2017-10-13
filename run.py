#!/usr/bin/env python3.5
from os import listdir
from os.path import isfile, join
import csv
import os
from dotenv import load_dotenv, find_dotenv
from ckanapi import RemoteCKAN
import ServiceRegistrationPipeline

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


def read_structure_from_last_run(filename):
    previous_file = "{dir}{filename}".format(
        dir=ARCHIVE_DIR, filename=filename)

    with open(previous_file) as csvfile:
        reader = csv.DictReader(csvfile)
        previous_headers = reader.fieldnames

    print(previous_headers)

    new_file = "{dir}{filename}".format(
        dir=FILES_TO_PUBLISH_DIR, filename=filename)
    with open(new_file) as csvfile:
        reader = csv.DictReader(csvfile)
        new_headers = reader.fieldnames

    print(new_headers)

    if(new_headers != previous_headers):
        raise StructureChangedException(previous_headers, new_headers)


def publish_fsd():
    files = ServiceRegistrationPipeline.find_files(FILES_TO_PUBLISH_DIR)

    for filename in files:
        read_structure_from_last_run(filename)

        # file_to_publish = "{dir}{filename}".format(
        #     dir=FILES_TO_PUBLISH_DIR, filename=filename)
        # print(file_to_publish)

        # # Publish
        # DATA_GOVT_NZ.action.resource_create(
        #     package_id=CKAN_PACKAGE_ID,
        #     url='dummy-value',  # ignored but required by CKAN<2.6
        #     upload=open(file_to_publish, 'rb'))

        # # Archive
        # archive_filename = "{dir}{filename}".format(
        #     dir=ARCHIVE_DIR, filename=filename)
        # os.rename(file_to_publish, archive_filename)


def delete_existing_resources():
    package = DATA_GOVT_NZ.action.package_show(id=CKAN_PACKAGE_ID)
    resources = package.get('resources')
    for r in resources:
        resource_id = r.get('id')
        DATA_GOVT_NZ.action.resource_delete(id=resource_id)

if __name__ == "__main__":
    publish_fsd()
