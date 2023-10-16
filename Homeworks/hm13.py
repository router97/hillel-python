# Homework 13 - Vladislav

import os
import shutil
from faker import Faker
faker = Faker()

""" Functions """
def fileCheck():
    try:
        os.mkdir('NEW DIR')
    except FileExistsError:
        pass
    open('NEW DIR/data.txt', 'a').close()

""" Choosing task """
while True:
    task = input("enter 1 to read, 2 to write, 3 to generate data: ")
    if task == '1' or task == '2' or task == '3':
        break
    else:
        print('invalid input!')
        continue

""" File reading """
if task == '1':
    fileCheck()
    with open('NEW DIR/data.txt', 'r') as fl:
        lines = fl.readlines()
        lines = [str(line).replace("\n", "").split(",") for line in lines]
        keys = [x for x in range(len(lines))]
        linesDict = {key: lines[key] for key in keys}
        for key,value in linesDict.items():
            print(f"{key} - {value}")

""" File writing """
if task == '2':
    fileCheck()
    while True:
        with open('NEW DIR/data.txt', 'a') as fl:
                print("name: ", end='')
                fl.write(f"{input().replace(',', '')},".capitalize())
                print("surname: ", end='')
                fl.write(f"{input().replace(',', '')},".capitalize())
                print("email: ", end='')
                fl.write(f"{input().replace(',', '')}\n")

""" Generating data """
if task == '3':
    fileCheck()
    with open('NEW DIR/data.txt', 'w') as fl:
        for i in range(5):
            fl.write(f"{faker.first_name()},{faker.last_name()},")
            fl.write(f"{faker.email()}\n")