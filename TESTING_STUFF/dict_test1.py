# age_dict = {}
# while True:
#     input_name = input("enter name: ")
#     if input_name == 'end':
#         break
#     input_age = input("enter age: ")
#     if input_age == 'end':
#         break
#     age_dict[input_name] = input_age
# print(age_dict) 
# key_values = {}
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# # zipped_key_values = zip((keys, values))
# # print(zipped_key_values)
# # for key, value in zip(keys, values):
# #     key_values[key] = value
# # print(key_values)

# for i in range(len(keys)):
#     key_values[keys[i]] = values[i]
# print(key_values)

# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# dict1.update(dict2)
# print(dict1)

# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }

# print(sampleDict["class"]["student"]["marks"]["history"])
# dict1 = {}
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# for i in range(0, len(employees)):
#     dict1[employees[i]] = defaults
# print(dict1)

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# # Keys to extract
# keys = ["name", "salary"]

# def extr(dict, key1, key2):
    
#     dict_extr = dict[key1] + dict[key2]
#     return dict_extr
# print(extr(sample_dict, "name", "salary"))

x= 10.9
print(x)
int(x)
print(x)