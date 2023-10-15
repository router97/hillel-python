# Homework 13 - Vladislav

""" Task 1 - List, Tuple """
list1 = ["red", "blue", "green"]
tuple1 = tuple(len(element) for element in list1)
print(f"Task 1: {tuple1} - len tuple") 
print(f"        {sum(tuple1)} - sum")

""" Task 2 - Set """
set1 = {element for element in range(1, 11)}
set2 = {element for element in range(5, 16)}
print(f"\nTask 2: {set1} , {set2} - set")

print(f"        {set1.union(set2)} - union")
print(f"        {set1.difference(set2)} - difference")
print(f"        {set1.intersection(set2)} - intersection")