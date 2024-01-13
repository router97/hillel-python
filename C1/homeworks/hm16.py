# Homework 16 - Vladyslav

from faker import Faker
from random import randint
faker = Faker()

def generate_students_and_grades_dict():
    """Generating random students, grades."""
    students = [faker.first_name() for _ in range(10)] # список 10 рандомных имён
    grades = [[randint(0,100) for _ in range(3)] for _ in range(10)] # список с 10 под-списками по 3 рандомных числа
    return {student: grade for student,grade in zip(students, grades)} # складываю всё в словарь -  {имя: [три числа]}

def averageGrades(grades):
    """Finding the average grade."""
    return {student: sum(grade)/len(grade) for student, grade in grades.items()} # возвращаю словарь - {имя: средняя оценка}

grades_dict = generate_students_and_grades_dict() # вызываю функцию
average_dict = averageGrades(grades_dict) # вызываю функцию

""" Output """
print('GRADES:')
for student, grade in grades_dict.items(): 
    print(f"\t{student}: {grade}")

print('\n\nAVERAGE:')
for student, average in average_dict.items(): 
    print(f"\t{student}: {average:.1f}") # округлил до 1 числа после запятой