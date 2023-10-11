# Homework 2 - Vladislav

str1 = input("Строка 1: ")
str2 = input("Строка 2: ")
str3 = input("Строка 3: ")

# task 1 ---------------

# sum of the lenghts of all inputs
AllLen = len(str1) + len(str2) + len(str3)
print("Завдання 1: Довжина", AllLen )

# task 2 ---------------

# finding the longest input
BiggestLen = 0

# checking if one input is longer than the other 2
if len(str1) > len(str2) and len(str1) > len(str3):
    BiggestLen = 1
elif len(str2) > len(str1) and len(str2) > len(str3):
    BiggestLen = 2
elif len(str3) > len(str2) and len(str3) > len(str1):
    BiggestLen = 3

# checking if all inputs are the same lenght
if BiggestLen == 0 and len(str1) == len(str2) and len(str2) == len(str3):
    print("Завдання 2: Усі строки однакової длини")
    BiggestLen = 4

# checking which 2 inputs are the longest (if there are 2 inputs equal) 
if BiggestLen == 0 and len(str1) == len(str2):
    print("Завдання 2: Найбільша 1 та 2 строка")
if BiggestLen == 0 and len(str1) == len(str3):
    print("Завдання 2: Найбільша 1 та 3 строка")
if BiggestLen == 0 and len(str2) == len(str3):
    print("Завдання 2: Найбільші 2 та 3 строки")

# checking which single input is the biggest (if they aren't the same, or 2 of them aren't equal)
if BiggestLen != 0 and BiggestLen != 4:
    print("Завдання 2: Найдовша", BiggestLen, "строка")



# task 3 ---------------

# finding the middle of each input

# if lenght is odd
if len(str1) % 2 == 1:   
    mid1 = len(str1) // 2
    even1 = False
if len(str2) % 2 == 1:
    mid2 = len(str2) // 2
    even2 = False
if len(str3) % 2 == 1:
    mid3 = len(str3) // 2
    even3 = False

# if lenght is even
if len(str1) % 2 == 0:   
    mid1 = len(str1) // 2
    even1 = True
if len(str2) % 2 == 0:
    mid2 = len(str2) // 2
    even2 = True
if len(str3) % 2 == 0:
    mid3 = len(str3) // 2
    even3 = True

# printing the middle digits, or saying the string is empty and doesn't have a middle
try:
    if even1 == False:
        print("Завдання 3: Середина Строка 1 ", str1[mid1])
    if even1 == True:
        print("Завдання 3: Середина Строка 1 ", str1[mid1 - 1], str1[mid1]) 
except IndexError:
    print("Завдання 3: Строка 1 пуста, неможна знайти середину")

try:
    if even2 == False:  
        print("Середина Строка 2 ", str2[mid2]) 
    if even2 == True:
        print("Середина Строка 2 ", str2[mid2 - 1], str2[mid2])
except IndexError:
    print("Строка 2 пуста, неможна знайти середину")

try:
    if even3 == False:
        print("Середина Строка 3 ", str3[mid3]) 
    if even3 == True:
        print("Середина Строка 3 ", str3[mid3 - 1], str3[mid3]) 
except IndexError:
    print("Строка 3 пуста, неможна знайти середину")