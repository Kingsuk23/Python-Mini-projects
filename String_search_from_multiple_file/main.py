import os

text=input("Enter text: ")
path=input("Enter path: ")

def getString(path):
    f=0
    os.chdir(path)
    files=os.listdir()
    for file_name in files:
        abs_path=os.path.abspath(file_name)
        if os.path.isdir(abs_path):
            getString(abs_path)
        if os.path.isfile(abs_path):
            f=open(file_name,'r')
            if text in f.read():
                f=1
                print(text + " found in ")
                final_path=os.path.abspath(file_name)
                print(final_path)
                return True
    if f==1:
        print(text + " not found! ")
        return False



getString(path)