# Homework 14 - Vladislav

import os
import shutil
import json

""" Choosing task """
while True:
    task = input("enter 1 to write and print data, 2 for data types: ")
    if task == '1' or task == '2':
        break
    else:
        print('invalid input!')
        continue