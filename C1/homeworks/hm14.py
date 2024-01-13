# Homework 14 - Vladyslav



# IMPORTS
import json



# CHOOSING TASK
while True:
    """Choosing task."""
    task = input("enter 1 for user, 2 for data types: ")
    if task == '1' or task == '2':
        break
    else:
        print('invalid input!')
        continue



# VARIABLES
user_dict = {}
type_dict = {
        "str": "a string",
        "int": 10,
        "float": 10.1,
        "list": [1,2,3],
        "dict": {"key": "value"},
        "bool": True 
        }



# FUNCTIONS
def json_write_input(input_dict):
    input_dict["name"] = input("Name: ")
    input_dict["age"] = input("Age: ")
    input_dict["address"] = input("Address: ")
    return input_dict


def json_write(path, dict1):
    with open(path, "w") as fl:
        fl.write(json.dumps(dict1, indent=4))


def json_read(path):
    print("reading:")
    with open(path, "r") as fl:
        json_data = json.load(fl)
        for key, value in json_data.items():
            print(f"\t{key}: {value}")


def json_read_types(path):
    print("reading:")
    with open(path, "r") as fl:
        json_data = json.load(fl)
        for key, value in json_data.items():
            print(f"\t{key}: {value}, {type(value)}")



# CALLING FUNCTIONS
if task == '1':
    user_dict = json_write_input(user_dict)
    json_write("user_data.json", user_dict)
    json_read("user_data.json")


if task == '2':
    json_write("data.json", type_dict)
    json_read_types("data.json")