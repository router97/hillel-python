# Homework 4 - Vladislav
number = ''
task = input("type 1 for multiplication table, 2 for grades: ")

# task 1 - multiplication table

while task == '1':
    while number.isdigit() == False: 
        number = input("input number>>")
        
    number = int(number)
    for i in range(2, 10):
        print(number,'x', i, '=', number * i)
    number = ''

# task 2 - grades

grade1 = '99'
grade2 = '99'
grade3 = '99'
grade4 = '99'


while task == '2':
    for g in range(4):
        while grade1.isdigit() == False or int(grade1) > 12:
            grade1 = input("grade 1: ")
            
        while grade2.isdigit() == False or int(grade2) > 12 :
            grade2 = input("grade 2: ")
            
        while grade3.isdigit() == False or int(grade3) > 12 :
            grade3 = input("grade 3: ")
            
        while grade4.isdigit() == False or int(grade4) > 12:
            grade4 = input("grade 4: ")
            
        
        sum = (int(grade1) + int(grade2) + int(grade3) + int(grade4))
        print("sum of your grades is:", sum)
        print("your average grade is:", sum // 4)
        grade1 = '99'
        grade2 = '99'
        grade3 = '99'
        grade4 = '99'
        