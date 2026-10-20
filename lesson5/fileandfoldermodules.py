import os
import shutil


def create_directory(directory):
    try:
        os.makedirs(directory)
    except OSError as exception:
        print(exception)

def delete_foler(path):
    empty = True
    for _ in os.scandir(path):
        empty = False
        break

    if empty:
        shutil.rmtree(path, ignore_errors=True)
    else:
        raise OSError(f"התיקייה '{path}' אינה ריקה ולכן לא ניתן למחוק אותה.")

def create_file(path):
    with open(path, 'x') as new_file:
        new_file.write("")

def delete_file(path):
    if os.path.exists(path):
        os.remove(path)

def write_file(path, content):
    with open(path, 'x') as new_file:
        new_file.write(content)

def list_files(path):
    if os.path.exists(path):
        files = os.listdir(path)
        return files
    else:
        raise OSError(f"<UNK> '{path}' <UNK> <UNK> <UNK> <UNK> <UNK>.")

def show_path(path):
    if os.path.exists(path):
        print(path)