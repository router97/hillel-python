# Homework 3 - Vladyslav

num_input = None
error_count = False

while True:
    task = input("enter 1 for palindromes, 2 for digits, 3 for password: ")
    if task == '1' or task == '2' or task == '3':
        break
    else:
        print('invalid input!')
        continue

# task 1 - palindromes

while task == '1':
    str1 = input("Слово: ")
    str2 = str1[::-1]

    if str.isspace(str1) == True or str1 == '':
        print("no input detected")
        error_count = True
    if str1 == str2 and error_count == False:
        print("Это палиндром")
    if str1 != str2 and error_count == False:
        print("Это не палиндром")

# task 2 - digits

num_input = 'h'
while task == '2':
    while num_input.isdigit() == False or len(num_input) != 2:
            num_input = (input("Enter a two-digit number: "))
        
            if len(num_input) != 2:
                continue
            if len(num_input) == 2 and num_input.isdigit() == True:
                break
    
    num = num_input[0:2]
    if int(num[0]) > int(num[1]):
        print("\t first digit", num[0], "is bigger than the second", num[1])
        num_input = 'h'
        continue
        
    if int(num[0]) < int(num[1]):
        print("\t second digit", num[1], "is bigger than the first", num[0])
        num_input = 'h'
        continue

    if int(num[0]) == int(num[1]):
        print("\t both digits are equal")
        num_input = 'h'
        continue

# task 3 - password

while task == '3':
    password = input("Enter your password: ")
    correct = 0
    
    
    if len(password) > 6:
        correct += 1
    else:
        correct -= 1

    if password.translate('0' and '1' and '2' and '3' and '4' and '5' and '6' and '7' and '8' and '9' and '0').islower() == True:
        correct -= 1
    else:
        correct += 1
    
    if password.isalpha() == True or password.isdigit() == True or password.isspace() == True:
        correct -= 1
    else:
        correct += 1
    
    
    if correct == 3:
        print("password valid!")
    if correct != 3:
        print("password invalid!")
        