# while
# while - цикл з умовою на початк, умова виконується, поки є True то цикл виконується

# i = 0
# while i < 10:
#     print(i)
#     i += 1
    
# for i in range(10):
#     print(i)


# num1 = input("Введіть число: ")
# # while num1.isdigit() == False:
# while not num1.isdigit():
#     print("Ви ввели не число")
#     num1 = input("Введіть число: ")
# num1 = int(num1)

# Отримати від користувача 10 чисел та вивести їх суму
# suma = 0

# num1 = input("Введіть число: ")
# num2 = input("Введіть число: ")
# num3 = input("Введіть число: ")
# num4 = input("Введіть число: ")
# num5 = input("Введіть число: ")
# num6 = input("Введіть число: ")
# num7 = input("Введіть число: ")
# num8 = input("Введіть число: ")
# num9 = input("Введіть число: ")
# num10 = input("Введіть число: ")

# suma = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10

# print(suma)


# suma = 0
# for i in range(10):
#     num1 = input("Введіть число: ")
#     while not num1.isdigit():
#         print("Ви ввели не число")
#         num1 = input("Введіть число: ")
#     num1 = int(num1)
#     suma += num1
# print(suma)


# for q in range(int(input("Введіть число!!!:"))):
#     print(q)


# #Безкінечний цикл
# counter = 0
# # while True:
# #     counter += 1
# #     if counter % 100000 == 0:
# #         print(counter)
# #     if counter == 100000000:
# #         break
# # print("Кінець програми")
    
    
# # break - припиняє виконання циклу
# # continue - припиняє виконання поточної ітерації циклу та переходить до наступної ітерації   

# # counter = 0
# while counter < 4000: # Поки counter менше 4000
#     if not counter % 33:
#         print(counter, 'its 3')
#         counter += 1
#         continue
#     if not counter % 2:
#         print(counter, 'its 90')
#         counter += 1 
#         print(counter, 'devided by 3')
    
#     if counter >= 1000:
#         break
    
#     counter += 5
    
    
    
# =======================================
# [while] В бесконечном цикле приложение запрашивает 
# у пользователя числа. 
# Ввод завершается, как только пользователь 
# вводит слово ‘end’. После завершения ввода 
# приложение выводит сумму чисел.







# Пользователь вводит число n и цифру a.
# Определить, сколько раз цифра встречается
# в числе. (не использовать метод count)
# n = 12122235
# a = 2
# count = 4

# n = input("Введіть число: ")
# a = input("Введіть цифру: ")

# counter = 0
# for num in n:
#     if num == a:
#         counter +=1
# print(counter)



# # second
# for i in range(len(n)):
#     # print(i)
#     if n[i] == a:
#         count += 1
# print(f'Number {a} in {n} is {count} times')

# # third
# count_loop = 0
# while count_loop < len(n):
#     if n[count_loop] == a:
#         count += 1
#     count_loop += 1
# print(f'Number {a} in {n} is {count} times')


print(not 'lolL'.isupper())
print(not 'lol322L'.islower())
print(not 'lol3%22L'.isalnum())
print(not len('lol3%22L')<6)

if not len('lol3%22L')<6:
    print('Ведіть довший пароль')


# *
# **
# ***
# ****
# *****
for i in range(5):
    print("*"*(i+1))
    
#*****
#****
#***
#**
#*
print("+++++++++++++")
for i in range(5):
    print('*'*(5-i))

# *****
# -****
# --***
# ---**
# ----*
for i in range(5):
    print(" "*i+"*"*(5-i))


#    *
#   **
#  ***
# ****
#*****
for i in range(5):
    print('-'*(5-i-1)+"*"*(i+1))
    
print('1',end='\t')
print('3',end='\t')
print('5',end='\t')
print('lol')
print('kek')
