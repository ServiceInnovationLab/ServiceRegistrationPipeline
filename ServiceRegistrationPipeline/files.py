from os import listdir
from os.path import isfile, join
import csv

def find_files(files_dir):
    files = [f for f in listdir(files_dir) if isfile(
        join(files_dir, f))]
    return files



def ensure_data_structure_unchanged(filename, archive_dir, incoming_dir):
    previous_file = "{dir}{filename}".format(
        dir=archive_dir, filename=filename)

    with open(previous_file) as csvfile:
        reader = csv.DictReader(csvfile)
        previous_headers = reader.fieldnames


    new_file = "{dir}{filename}".format(
        dir=incoming_dir, filename=filename)
    with open(new_file) as csvfile:
        reader = csv.DictReader(csvfile)
        new_headers = reader.fieldnames

    if(new_headers != previous_headers):
        raise StructureChangedException(previous_headers, new_headers)
