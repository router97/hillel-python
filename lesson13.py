#File System
import os # модуль для работы с файловой системой
import shutil # модуль для работы с файлами и папками

print('hello')

# F:\DotPack Projects\HILLEL\NeuronsProgaTrojanGXc++JaWaC#PHP> lesson13/lesson13.py
# python lesson13/lesson13.py


#Повна адреса до файлу
# f:/DotPack Projects/HILLEL/NeuronsProgaTrojanGXc++JaWaC#PHP/lesson13/lesson13.py"

# Не повна адреса до файлу
# lesson13/lesson13.py


# abspath - повний шлях до файлу, який включає всі папки, в яких він знаходиться

print( os.path.abspath('ldfsdfsdfsdf.py'))
# os.mkdir('!TEST!')
# os.mkdir(r'F:\DotPack Projects\HILLEL\NeuronsProgaTrojanGXc++JaWaC#PHP\lesson13\LOLTEST')


# os.mkdir('F:\DotPack Projects\HILLEL\mindCodeComputerITgenius\lesson12\new_folder')
# os.mkdir('F:\\DotPack Projects\\HILLEL\\mindCodeComputerITgenius\\lesson12\\new_folder')
# os.mkdir(r'F:\DotPack Projects\HILLEL\mindCodeComputerITgenius\lesson12\new_folder')
# os.mkdir('F:/DotPack Projects/HILLEL/mindCodeComputerITgenius/lesson12/new_folder')

names= ['BMW', 'Audi', 'Mercedes', 'VW', 'Opel', 'Porsche', 'Ferrari', 'Lamborghini', 'Maserati', 'Bentley']



os.mkdir('lesson13/LOLTEST') # створити папку

for name in names:
    os.mkdir(f'lesson13/LOLTEST/{name}')

os.rmdir('lesson13/LOLTEST/BMW') # видалити папку, якщо вона пуста
os.rename('lesson13/LOLTEST/Audi', 'lesson13/LOLTEST/Toyota') # перейменувати папку
# os.rmdir('lesson13/LOLTEST') # видалити папку, якщо вона пуста

# list_dir = os.listdir('lesson13/LOLTEST') # список файлів і папок в папці
# print(list_dir)
# for item in list_dir:
#     os.rmdir('lesson13/LOLTEST/' +  item)
#     print(item + ' deleted')

shutil.rmtree('lesson13/LOLTEST') # видалити папку, якщо вона не пуста

# open('lesson13/LOLTEST/Toyota/1.txt', 'w').close() # створити файл
# os.remove('lesson13/LOLTEST/Toyota/1.txt') # видалити файл

# os.rmdir('lesson13/LOLTEST/Toyota') # видалити папку, якщо вона пуста

# shutil.rmtree('lesson13/LOLTEST') # видалити папку, якщо вона не пуста

# Валідація шляху
# is_ex = os.path.exists('lesson13\LOL') #- Перевірка чи існує папка
# print(is_ex)

if not os.path.exists('lesson13\LOL'):
    os.mkdir('lesson13\LOL')
else:
    print('Папка вже існує')
#     shutil.rmtree('lesson13\LOL')
#     os.mkdir('lesson13\LOL')


if os.path.exists('lesson13\LOL'):
    print('Папка вже існує')
    shutil.rmtree('lesson13\LOL')
os.mkdir('lesson13\LOL')



list_files_and_dirs = os.listdir('lesson13') #- Повертає список файлів і папок в папці
print(list_files_and_dirs)  

for i in list_files_and_dirs:
    if os.path.isdir('lesson13/' + i):
        print('Папка: ' + i)
    else:
        print('Файл: ' + i)


#FileS
# open() - ця функція дозволяє створювати, читати, редагувати і видаляти файли
# csv - це формат файлу, який використовується для зберігання даних у вигляді таблиці
# txt - це формат файлу, який використовується для зберігання даних у вигляді тексту
# json - це формат файлу, який використовується для зберігання даних у вигляді тексту

all_text = open('lesson13/lesson13.py', encoding='utf-8').read() #- Читання файлу
print(all_text)


# mode - режим роботи з файлом
# r - read - читання
# w - write - запис, якщо файлу не існує, то він створюється, якщо файл існує, то він перезаписується
# a - append - допис, якщо файлу не існує, то він створюється, якщо файл існує, то він дописується в кінець файлу
# b - binary - бінарний режим, використовується для роботи з бінарними файлами

# r+ - read and append - читання і запис
# w+ - write and read - запис і читання

#encoding - кодування файлу
# windows-1251
# cp1251
# utf-8


# fl = open('lesson13\\text.txt', 'w', encoding='utf-8') #- Відкриття файлу
# fl.write('Hello world\n') #- Запис в файл
# fl.write('Hello world2') #- Запис в файл
# fl.close() #- Закриття файлу



# контекстний менеджер - це спеціальний синтаксис, який дозволяє працювати з файлами
with open('lesson13/text.txt', 'w', encoding='utf-8') as fl:
    fl.write('Hello world\n')
    fl.write('\nHello world2')
    fl.write('\nHello world3')
    fl.write('\t\tHello world4')
print('file is closed')

# with open('lesson13/text.txt', 'a', encoding='utf-8') as fl:
#     fl.write('\n'+"="*50)
#     for i in range(10):
#         fl.write('\nHello world' + str(i))
    
# with open('lesson13/text.txt', 'r+', encoding='utf-8') as fl:
    
#     text = fl.read()
#     print(text)
#     fl.seek(10)
#     fl.write('"""ТУТ МОЖЕ БУТИ ВАША РЕКЛАМА"""')