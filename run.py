#!/usr/bin/env python3.5
import os
from dotenv import load_dotenv, find_dotenv
from ckanapi import RemoteCKAN


# Load config from .env
load_dotenv(find_dotenv())
CKAN_API_KEY = os.environ.get('CKAN_API_KEY')
CKAN_CLIENT_USER_AGENT = os.environ.get('CKAN_CLIENT_USER_AGENT')
CKAN_URL = os.environ.get('CKAN_URL')
CKAN_PACKAGE_ID = os.environ.get('CKAN_PACKAGE_ID')


def get_files_from_msd():
    return ['hello.txt', ]


def send_files_to_ckan(files):
    mysite = RemoteCKAN(CKAN_URL, apikey=CKAN_API_KEY,
                        user_agent=CKAN_CLIENT_USER_AGENT)

    for f in files:
        mysite.action.resource_create(
            package_id=CKAN_PACKAGE_ID,
            url='dummy-value',  # ignored but required by CKAN<2.6
            upload=open(f, 'rb'))

if __name__ == "__main__":
    files = get_files_from_msd()
    send_files_to_ckan(files)
