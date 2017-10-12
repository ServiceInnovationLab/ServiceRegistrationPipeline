from os import listdir
from os.path import isfile, join


def find_files(files_dir):
    files = [f for f in listdir(files_dir) if isfile(
        join(files_dir, f))]
    return files
