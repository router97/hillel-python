# Homework 1, Владислав
# Завдання 1 - калькулятор

task = None

print("Виберите калькулятор або місяці")

#цикл вибора
while task != 1 or task != 2:
    try:
        task = int(input("1 або 2: "))
    except ValueError:
        print("Помилка")
        continue
    if task == 1 or task == 2:
        break
    else:
        print("Помилка")
        continue

# цикл калькулятора
while task == 1:
    try:
        num1 =  int(input('Введіть перше число: '))
        num2 = int(input('Введіть друге число: '))
    except ValueError:
        print("Помилка")
        continue
    znak = input('Введіть знак(+, -, *, /, %, **, //): ')
    if znak == "+":
        print(num1 + num2)
    elif znak == "-":
        print(num1 - num2)
    elif znak == "*":
        print(num1 * num2)  
    elif znak == "/":
        if num2 == 0:
            print('Ділення на нуль заборонено')
        else:
            print(num1 / num2)
    elif znak == "%":
        if num2 == 0:
            print("Ділення на нуль заборонено")
        else:
            print(num1 % num2)
    
    elif znak == "**":
        print(num1 ** num2)
    elif znak == "//":
        if num2 == 0:
            print("Ділення на нуль заборонено")
        else:
            print(num1 // num2)
            
# Завдання 2 - місяці

# цикл місяців
while task == 2:
    try:
        MonthsInput = int(input("Введіть номер місяця: "))
    except ValueError:
        print("Помилка")
        continue
    if MonthsInput == 3 or MonthsInput == 4 or MonthsInput == 5:         
        print("Весна")
    elif MonthsInput == 6 or MonthsInput == 7 or MonthsInput == 8:
        print("Літо")
    elif MonthsInput == 9 or MonthsInput == 10 or MonthsInput == 11:
        print("Осінь")
    elif MonthsInput == 12 or MonthsInput == 1 or MonthsInput == 2:
        print("Зима")
    else:
        print("Помилка")
     
    
    
    