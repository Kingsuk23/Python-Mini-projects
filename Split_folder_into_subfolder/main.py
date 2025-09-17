import glob
import os
from shutil import copy2
import sys

def get_files(path):
    files= sorted(glob.glob(f'{path}/*'))
    return files

def get_full_path(path):
    return  os.path.abspath(path)

def copy_file(src,dst):
    if not os.path.isdir(dst):
        os.mkdir(dst)
    copy2(src,dst)

def split(data, count):

    for i in range(1,len(data),count):
        yield data[i:i + count]

def start_process(path,count):
    files=get_files(path)

    splited_data=split(files,count)
    for idx, folder in enumerate(splited_data):

        name = f'data_{idx}'
        print(idx)
        for file in folder:
            copy_file(get_full_path(file), get_full_path(name))


start_process("/home/user/Documents/Text File",2)