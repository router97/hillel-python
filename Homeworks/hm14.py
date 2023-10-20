# Homework 14 - Vladislav

import json

while True:
    """Choosing task."""
    task = input("enter 1 for user, 2 for data types: ")
    if task == '1' or task == '2':
        break
    else:
        print('invalid input!')
        continue

user_dict = {}
type_dict = {
        "str": "a string",
        "int": 10,
        "float": 10.1,
        "list": [1,2,3],
        "dict": {"key": "value"},
        "bool": True 
        }

def json_write_input(dict1):
    dict1 = {
        "name": input("Name: "),
        "age": input("Age: "),
        "address": input("Address: "),
    }
    return dict1

def json_write(path,dict1):
    with open(path, "w") as fl:
        fl.write(json.dumps(dict1, indent=4))

def json_read(path):
    print("reading:")
    with open(path, "r") as fl:
        json_data = json.load(fl)
        for key,value in json_data.items():
            print(f"\t{key}: {value}")

def json_read_type(path):
    print("reading:")
    with open(path, "r") as fl:
        json_data = json.load(fl)
        for key,value in json_data.items():
            print(f"\t{key}: {type(value)}")

if task == '1':
    user_dict = json_write_input(user_dict)
    json_write("user_data.json",user_dict)
    json_read("user_data.json")
if task == '2':
    json_write("data.json",type_dict)
    json_read_type("data.json")