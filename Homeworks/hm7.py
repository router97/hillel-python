# Homework 7 - Vladyslav

task = input("enter 1 for Colors, 2 for Odd List, 2alt for alt Odd List: ")

# task 1 - Colors
color_count = 4
colors = []
colors_accept = ['red', 'orange', 'yellow', 'green', 'blue', 'violet', 'pink', 'cyan', 'brown']
while task == '1':
    for color in range(color_count):
        color = input("color: ")
        if color in colors_accept:
            colors.append(color)
        else:
            print("invalid color")
            continue
    if len(colors) == 4:
        print(colors)
        colors = []
    
# task 2 - Odd List

# this is returning only the  1st, 3rd, 5th etc. input

numbers = []
while task == '2':
    while True:
        number = input("enter your number: ")
        if not number == 'end' and number.isdigit() == False:
            print("error")
            break
        if number == 'end':
            break
        numbers.append(number)
    print(numbers[::2])
    numbers = []
    
# task 2 - Odd List (alt)

# this is returning odd inputs

numbers_accept = []
while task == '2alt':
    while True:
        number = input("enter your number: ")
        if not number == 'end' and number.isdigit() == False:
            print("error")
            break
            
        if number == 'end':
            break
        numbers.append(number)
    for number in numbers:
        if int(number) % 2 > 0:
            numbers_accept.append(number)
    print(numbers_accept)
    numbers = []
        