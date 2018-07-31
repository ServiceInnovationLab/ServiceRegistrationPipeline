#!/usr/bin/env python
"""
Reads files in the FILES_TO_PUBLISH_DIR
checks they have the same structure as the last time (in ARCHIVE_DIR)
if the same, the publish on CKAN
"""

from os import listdir
from os.path import isfile, join, exists
from dotenv import load_dotenv, find_dotenv
from ckanapi import RemoteCKAN
import csv
import os

# Load config from .env
load_dotenv(find_dotenv())

CKAN_API_KEY = os.environ.get('CKAN_API_KEY')
CKAN_CLIENT_USER_AGENT = os.environ.get('CKAN_CLIENT_USER_AGENT')
CKAN_URL = os.environ.get('CKAN_URL')
CKAN_PACKAGE_ID = os.environ.get('CKAN_PACKAGE_ID')

FILES_TO_PUBLISH_DIR = os.environ.get('FILES_TO_PUBLISH_DIR')
ARCHIVE_DIR = os.environ.get('ARCHIVE_DIR')

CKAN_REMOTE = RemoteCKAN(CKAN_URL, apikey=CKAN_API_KEY,
                          user_agent=CKAN_CLIENT_USER_AGENT)


def find_files(files_dir):
    files = [f for f in listdir(files_dir) if isfile(
        join(files_dir, f))]
    return files

def does_file_exist(file):
    return os.path.exists(file)

def ensure_data_structure_unchanged(filename, archive_dir, incoming_dir):
    previous_file = "{dir}{filename}".format(
        dir=archive_dir, filename=filename)
    
    if does_file_exist(previous_file):
        pass
    else: # If no file exists it's a new file so we wont need to comapre the structure
        print('New file to upload.')
        return
    
    with open(previous_file) as csvfile:
        reader = csv.DictReader(csvfile)
        previous_headers = reader.fieldnames

    new_file = "{dir}{filename}".format(
        dir=incoming_dir, filename=filename)
        
    with open(new_file) as csvfile:
        reader = csv.DictReader(csvfile)
        new_headers = reader.fieldnames

    if(new_headers != previous_headers):
        difference = set(new_headers) - set(previous_headers)
        raise SystemExit("Data structure changed, stop the upload: {difference}".format(difference=difference))
    else:
        print('File is same structure as previous file upload, ok to continue.')
    
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
    package = CKAN_REMOTE.action.package_show(id=CKAN_PACKAGE_ID)
    return package.get('resources')


def update_existing_resource(filename, resource_id):
    print("Update {filename}".format(filename=file_to_publish(filename)))
    CKAN_REMOTE.action.resource_update(
        id=resource_id, upload=open(file_to_publish(filename), 'rb'))


def create_new_resource(filename):
    print("Publishing new resource.")
    CKAN_REMOTE.action.resource_create(
        package_id=CKAN_PACKAGE_ID, description=filename,
        upload=open(file_to_publish(filename), 'rb'))


def delete_all_existing_resources():
    package = CKAN_REMOTE.action.package_show(id=CKAN_PACKAGE_ID)
    resources = package.get('resources')
    for r in resources:
        resource_id = r.get('id')
        CKAN_REMOTE.action.resource_delete(id=resource_id)


def file_to_publish(filename):
    return "{dir}{filename}".format(
        dir=FILES_TO_PUBLISH_DIR, filename=filename)

if __name__ == "__main__":
    files = find_files(FILES_TO_PUBLISH_DIR)

    for filename in files:

        if filename == '.keep':
            print("Skipping .keep")
        else:
            print(filename)

            print("Checking file structure...")
            ensure_data_structure_unchanged(
                filename, archive_dir=ARCHIVE_DIR,
                incoming_dir=FILES_TO_PUBLISH_DIR)

            resource_id = find_existing_resource_id(filename)

            if (resource_id):
                print("Publishing update to CKAN")
                # TODO: Check if file is identical
                update_existing_resource(filename, resource_id)
            else:
                print("Creating new resource on CKAN")
                create_new_resource(filename)

            print("Saving archive copy.")
            archive_file(filename)
