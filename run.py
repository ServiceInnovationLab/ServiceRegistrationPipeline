#!/usr/bin/env python
from os import listdir
from os.path import isfile, join
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


def find_existing_resource_id(filename):
    resources = existing_resources()
    for r in resources:
        if r.get('description') == filename:
            return r.get('id')


def archive_file(filename):
    archive_filename = "{dir}{filename}".format(
        dir=ARCHIVE_DIR, filename=filename)
    os.rename(file_to_publish(filename), archive_filename)


def existing_resources():
    package = DATA_GOVT_NZ.action.package_show(id=CKAN_PACKAGE_ID)
    return package.get('resources')


def update_existing_resource(filename, resource_id):
    print("update {filename}".format(filename=file_to_publish(filename)))
    DATA_GOVT_NZ.action.resource_update(
        id=resource_id, upload=open(file_to_publish(filename), 'rb'))


def create_new_resource(filename):
    print("Publishing new resource.")
    DATA_GOVT_NZ.action.resource_create(
        package_id=CKAN_PACKAGE_ID, description=filename, upload=open(file_to_publish(filename), 'rb'))


def delete_all_existing_resources():
    package = DATA_GOVT_NZ.action.package_show(id=CKAN_PACKAGE_ID)
    resources = package.get('resources')
    for r in resources:
        resource_id = r.get('id')
        DATA_GOVT_NZ.action.resource_delete(id=resource_id)


def file_to_publish(filename):
    return "{dir}{filename}".format(
        dir=FILES_TO_PUBLISH_DIR, filename=filename)

if __name__ == "__main__":
    files = ServiceRegistrationPipeline.find_files(FILES_TO_PUBLISH_DIR)

    for filename in files:

        if filename == '.keep':
            print("Skipping .keep")
        else:
            print(filename)

            print("Checking file structure is same as last.")
            ServiceRegistrationPipeline.ensure_data_structure_unchanged(
                filename, archive_dir=ARCHIVE_DIR, incoming_dir=FILES_TO_PUBLISH_DIR)

            resource_id = find_existing_resource_id(filename)

            if (resource_id):
                update_existing_resource(filename, resource_id)
            else:
                create_new_resource(filename)

            print("Saving archive copy.")
            archive_file(file_to_publish)
