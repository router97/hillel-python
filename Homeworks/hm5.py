# Homework 5 - Vladyslav

height = ''

task = input("enter 1 for triangle, 2 for multiplication table: ")

# task 1 - Triangle

while task == '1':
    height = ''
    while height.isdigit() == False:
        height = input("enter: ")
        height2 = height
    if not int(height) < 16:
        height = ''
        continue
    if not int(height) > 16:
        height = int(height)
        for i in range(height):
            print('-'*(i)  +  "*"*((height)*2-1))
            height -= 1

# task 2 - Multiplication Table

mulnum = 1
if task == '2':
    print("\t1\t2\t3\t4\t5\t6\t7\t8\t9")
    for h in range(9):
        print(mulnum, end = '')
        for i in range(1, 10):
            print("\t", mulnum * i, end = '')
            if i == 9:
                mulnum += 1
                print("\n")