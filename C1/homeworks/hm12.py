# Homework 12 - Vladyslav


import os 
import shutil
import time

while True:
    task = input("enter 1 for directories, 2 for files, 3 to delete files: ")
    if task == '1' or task == '2' or task == '3':
        break
    else:
        print('invalid input!')
        continue

""" Task 1 - directory work """

def dir_func(var): # creates, moves, copies, deletes files
    try:
        if var == 1:
            os.mkdir('NEW DIR')
            open('NEW DIR/NEW FILE.txt', 'w').close()
            open('NEW DIR/NEW FILE2.txt', 'w').close()
            print("created")
    except FileExistsError:
        shutil.rmtree("NEW DIR")
        os.mkdir('NEW DIR')
        open('NEW DIR/NEW FILE.txt', 'w').close()
        open('NEW DIR/NEW FILE2.txt', 'w').close()
        print("created")
    if var == 2:
        os.mkdir("NEW DIR\\NEWER DIR")
        shutil.move("NEW DIR/NEW FILE.txt", "NEW DIR/NEWER DIR")
        print("moved")
    if var == 3:
        shutil.copy("NEW DIR/NEWER DIR/NEW FILE.txt", "NEW DIR/NEW FILE.txt")
        shutil.copytree("NEW DIR", "NEW DIR/NEW DIR COPY")
        print("copied")
    if var == 4:
        shutil.rmtree("NEW DIR")
        print("deleted")
if task == '1':
    dir_func(1)
    time.sleep(4)
    dir_func(2)
    time.sleep(4)
    dir_func(3)
    time.sleep(8)
    dir_func(4)


""" Task 2 - file editing """

def file_func(var): # creates a file, lets you write 5 lines then read the file in a loop
    try:
        os.mkdir('NEW DIR')
    except FileExistsError:
        shutil.rmtree("NEW DIR")
        os.mkdir('NEW DIR')
    while var == 1:
        with open("NEW DIR\\NEW FILE.txt", "a") as fl:
            fl.write(input("write: ") + "\n" )
        with open("NEW DIR\\NEW FILE.txt", "r") as fl:
            print(fl.read())
if task == '2':
    file_func(1)


""" Delete everything """
if task == '3':
    shutil.rmtree("NEW DIR") # delete everything made by the programm