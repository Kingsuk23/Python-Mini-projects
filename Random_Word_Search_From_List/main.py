import random
import sys

if sys.argv[1:]:
    filename=sys.argv[1]
else:
    filename=input("Enter file name: ")

    try:
        file=open(filename)
    except(FileNotFoundError,IOError):
        print("File does not exist")
        exit()

    number_of_lines=sum(1 for line in file if line.strip())

    random_line=random.randint(0,number_of_lines)

    file.seek(0)

    for i, line in enumerate(file):
        if i==random_line:
            print(line.rstrip())
            break