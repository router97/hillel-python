#Set,tuple

from sys import getsizeof
from random import randint



"""String"""
# Строка - це не змінний тип данних, яка містить в собі послідовність символів

#Properties
# 1. Не змінний тип данних (immutable) - не можна змінити один символ в строці
# 2. Ітерабельний тип данних (iterable) - можна ітерувати по символах
# 3. Індексований тип данних (indexable) - можна отримати доступ до символів по індексу
# 4. Зрізи (slices) - можна отримати підстроку
# 5. Cклеювання (concatenation) - можна склеїти дві строки "1" + "2" = "12"
# 6. Повторення (repetition) - можна повторити строку "1" * 3 = "111"
# 7. Форматування (formatting) - можна форматувати строку
# 8. Методи (methods) - можна викликати методи для роботи зі строкою

# a = 'Hello world'
# # a[4] = 'a' # TypeError: 'str' object does not support item assignment
# a = a.replace('o', 'a')
# print(a)
# a = '[1, 2, 3]'
# a = a[1:-1]

# Плюси:
    # 1. Багато методів для роботи зі строками
    # 2. Простота використання - легко створити і використати, можна використовувати в інших типах данни
    # 3. Займає мало пам'яті
    
# Мінуси:
    # 1. Не змінний тип данних - не можна змінити один символ в строці
    
    
# a = '1234'
# print(getsizeof(a))
# a = ''
# print(getsizeof(a))    
# a= '1'
# print(getsizeof(a))



"""List"""
# Список - це змінний тип данних, який містить в собі послідовність об'єктів

# Properties
# 1. Змінний тип данних (mutable) - можна змінити один елемент в списку
# 2. Ітерабельний тип данних (iterable) - можна ітерувати по елементах
# 3. Індексований тип данних (indexable) - можна отримати доступ до елементів по індексу
# 4. Зрізи (slices) - можна отримати підсписок
# 5. Cклеювання (concatenation) - можна склеїти два списки [1, 2] + [3, 4] = [1, 2, 3, 4]
# 6  Повторення (repetition) - можна повторити список [1, 2] * 3 = [1, 2, 1, 2, 1, 2]
# 7. Методи (methods) - можна викликати методи для роботи зі списком
# 8. Можна містити в собі різні типи данних
# 9. простота в доступі до елементів по індексу a[0] = 1  a[1], a[2], a[3] = 2, 3, 4
# 10. list comprehension - можна створити список за допомогою генератора списку

# Плюси:
    # 1. Багато методів для роботи зі списками
    # 2. Mutable - можна змінити один елемент в списку
    # 3. Простота використання - легко створити і використати, можна використовувати в інших типах данни
    # 4. Займає мало пам'яті. Третій за розміром тип данних
    
# Мінуси:
    #1. Займає багато пам'яті, якщо в списку багато елементів
    
    
a = [1,2,3]
print(getsizeof(a))
a = []
print(getsizeof(a))
a = [1]
print(getsizeof(a))
a = [1,2]
print(getsizeof(a))
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,"sdasdsadasdasdadafssdfsdfgsdfasdfdfasdfasdfasdfasfvsadfafbadfvafdvasfdasdf"]
print(getsizeof(a))

a = [randint(1, 100) for i in range(10000)]
print(getsizeof(a))
a = [randint(1, 100) for i in range(100000)]



"""Tuple"""

# Кортеж - це не змінний тип данних, який містить в собі послідовність об'єктів

(1,)
# # (,)
# 1,2,3,4
# a = (1,2,3,4)
# a= 1,2,3,4
# a = 1,
# a = ()
# print(type(a))

# def func():
#     a = 1
#     b = 2
#     c = a + b
#     return a, b, c

# a = func()
# print(a[0], a[1], a[2])

# a1, a2, a3 = func()
# print(a1, a2, a3)

# a[i] , a[i+1] = a[i+1], a[i]

# fruits = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
# # for i in range(len(fruits)):
# #     print(i+1, fruits[i])
    
    
# # for fruit in fruits:
# #     print(fruit)
    
# enumerate(fruits) # [(0, 'apple'), (1, 'banana'), (2, 'cherry'), (3, 'orange'), (4, 'kiwi'), (5, 'melon'), (6, 'mango')]

# for a ,fruit in enumerate(fruits,10):
#     print(f'{a}. {fruit}')


# Properties
# 1. Не змінний тип данних (immutable) - не можна змінити один елемент в кортежі
# 2. Ітерабельний тип данних (iterable) - можна ітерувати по елементах
# 3. Індексований тип данних (indexable) - можна отримати доступ до елементів по індексу
# 4. Зрізи (slices) - можна отримати підкортеж
# 5. Cклеювання (concatenation) - можна склеїти два кортежі (1, 2) + (3, 4) = (1, 2, 3, 4)
# 6  Повторення (repetition) - можна повторити кортеж (1, 2) * 3 = (1, 2, 1, 2, 1, 2)
# 7. Методи (methods) - можна викликати методи для роботи з кортежем
# 8. Можна містити в собі різні типи данних

# Плюси == мІнуси:
    # 2. Не змінний тип данних - не можна змінити один елемент в кортежі
    # 3. Простота використання - легко створити і використати, можна використовувати в інших типах данни
    # 4. Займає мало пам'яті.
    

# a = (1,2,3)
# print(getsizeof(a))
# a = ()
# print(getsizeof(a))
# a = ('1','2','3','4','5','6','7','8','9')
# print(getsizeof(a))
# a= tuple()

# a = tuple(i for i in range(10))
# a = sum(i for i in range(10))
# a= (i for i in range(10))
# print(a)


"""SET"""
# {}
# # Сет - це не змінний тип данних, який містить не упорядковану послідовність унікальних об'єктів
# set1 = {1,1,1,1,1,2,2,2,2,34,3,3,3,3,3,4,4,4,5,6,6,6,7,7,8,98,8,5,2,3,4,2,1,2,3,1,2,3}
# print(set1)
# print(getsizeof(set1))

# dic1 = {'a':1, 'b':2, 'c':3}
# set2 = {1,2,3}
# print(getsizeof(set2))
# print(getsizeof(dic1))

# set2.add([1,2,3])
# print(set2)


# Тип даних	 Змінність	Приклади
# Immutable	 Незмінний	int, float, bool, str, tuple, frozenset
# Mutable	 Змінний	 list, dict, set


# Properties
# 1. змінний тип данних (mutable) - не можна змінити один елемент в сеті
# 2. Неіндексований тип данних (unindexable) - не можна отримати доступ до елементів по індексу
# 3. не упорядкований тип данних (unordered) - не можна отримати доступ до елементів по індексу 
# 4. Зрізи (slices) - не можна отримати підсет
# 5. Cклеювання (concatenation) - не можна склеїти два сети {1, 2} + {3, 4} = TypeError: unsupported operand type(s) for +: 'set' and 'set'
# 6. Підтримує багато методів (methods) - можна викликати методи для роботи з сетом

# № Плюси:
    # 1.Унікальність елементів - в сеті може бути тільки унікальні елементи


# № Мінуси:
    # 1.Багато памяті - займає багато памяті
    

a = {1,2,3}
print(getsizeof(a))

a = set()
print(getsizeof(a))

a = {1,2,3,4,5,6,7,8,9,10,11,12,13,"sda"}
print(getsizeof(a))




set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

# Difference - різниця між двома сетами

print(set1.difference(set2))
print(set2.difference(set1))

print(set1 - set2)

# Intersection - перетин двох сетів
print(set1.intersection(set2))
print(set2.intersection(set1))

print(set1 & set2)

#Symmetric difference - симетрична різниця двох сетів
print(set1.symmetric_difference(set2))
print(set2.symmetric_difference(set1))

print(set1 ^ set2)

#Методи для роботи з сетами які змінюють сет

print(set1)

# set1.difference_update(set2)
# set1 -= set2
# set1 = set1 - set2

print(set1)

# set1.intersection_update(set2)
# set1 &= set2
# set1 = set1 & set2

print(set1)

# set1.symmetric_difference_update(set2)
# set1 ^= set2
# set1 = set1 ^ set2


# set1.update(set2) #- додає елементи з set2 в set1
print(set1)

set1.add(100) # - додає елемент в сет
print(set1)
set1.add(100)
print(set1)

set1.remove(100) # - видаляє елемент з сету
print(set1)

a = set1.pop() # - видаляє елемент з сету і повертає його
print(set1, a)

 # - об'єднує два сети
print(set1.union(set2))

# set1.clear() # - очищає сет
# print(set1)




# l = []
# l.append(set1.pop())
# print(l)
# l.append(set1.pop())
# print(l)

# a = list(set1)
# a.sort()
# a = set(a)
# print(a)


import time  # time - модуль для роботи з часом
import datetime # datetime - модуль для роботи з датою і часом

import random # random - модуль для роботи з випадковими числами
import sys # sys - модуль для роботи з системою (перемінні середовища, аргументи командного рядка, і т.д.)
print(sys.argv) # sys.argv - список аргументів командного рядка

import os # os - модуль для роботи з операційною системою
print(os.getcwd()) # os.getcwd() - повертає поточну директорію

import math # math - модуль для роботи з математичними функціями
print(math.pi) # math.pi - число пі
print(math.pow(2,5)) # math.pow(x,y) - x в степені y
print(math.sqrt(25)) # math.sqrt(x) - квадратний корінь з x

import re # re - модуль для роботи з регулярними виразами

some_email = "LOasdaL@lol.ua"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
if re.match(pattern, some_email):
    print("Valid email")
else:
    print("Invalid email")

import json # json - модуль для роботи з json

import csv # csv - модуль для роботи з csv

import logging # logging - модуль для роботи з логами

import sqlite3 # sqlite3 - модуль для роботи з базами даних sqlite3

import smtplib # smtplib - модуль для роботи з поштою

import requests # requests - модуль для роботи з HTTP запитами

import turtle # turtle - модуль для роботи з графікою

import tkinter # tkinter - модуль для роботи з графічним інтерфейсом користувача

import winsound # winsound - модуль для роботи зі звуком

# winsound.Beep(1000, 1000) # winsound.Beep(frequency, duration) - відтворює звук з частотою frequency і тривалістю duration
# winsound.Beep(300,200)
# winsound.Beep(425,200)
# winsound.Beep(285,200)
# winsound.Beep(285, 300)
# winsound.Beep(325, 200)
# winsound.Beep(365, 200)
# winsound.Beep(315, 200)

# for i in range(1, 100):
#     winsound.Beep(i*37, 100)
    
    
from pygame import mixer # mixer - модуль для роботи зі звуком
mixer.init() # mixer.init() - ініціалізує mixer
mixer.music.load("lesson16/reflected-light-147979.mp3") # mixer.music.load("music.mp3") - завантажує музичний файл
# mixer.music.set_volume(0.2) # mixer.music.set_volume(0.2) - встановлює гучність
mixer.music.play() # mixer.music.play() - відтворює музичний файл
mixer.music.set_volume(0.05) # mixer.music.set_volume(0.2) - встановлює гучність
while mixer.music.get_busy():
    # time.sleep(1)
    print("Playing...")
    a = input("Q - stop")
    if a == "Q":
        mixer.music.stop()
        break