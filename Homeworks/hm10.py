# Homework 10 - Vladyslav


while True:
    task = input("enter 1 for multiplication, 2 for capitals: ")
    if task == '1' or task == '2':
        break
    else:
        print('invalid input!')
        continue


# task 1 - multiplication function


while task == '1':
    print("\ntype your numbers or type end to stop\n")
    input_list = []

    typing = True
    while typing == True:
        input_number = input("enter a number:")
        if input_number.isdigit() == True:
            input_list.append(int(input_number))
        elif input_number == 'end':
            if input_list != []:
                break
        else:
            print("invalid input")

    
    def multiplication_func(numbers):
        for index in range(1, len(numbers)):
            numbers[0] = numbers[0]*numbers[index]
        return numbers[0]
    print(multiplication_func(input_list))


# task 2 - capital, non-capital letters function


if task == '2':
    
    def letters_func(string):
        upper_counter = 0
        lower_counter = 0
        for letter in string:
            
            if letter.islower() == True:
                lower_counter += 1
            elif letter.isupper() == True:
                upper_counter += 1
            else:
                continue
            
        return lower_counter, upper_counter
    
    
    while task == '2':
        input_string = input("enter your string: ")
        (lower_counter, upper_counter) = letters_func(input_string)
        
        print("lowercase = {0}\nuppercase = {1}".format(lower_counter, upper_counter))