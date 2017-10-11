from os import listdir


def find_files(files_dir):
    files = [f for f in listdir(files_dir) if isfile(
        join(files_dir, f))]
