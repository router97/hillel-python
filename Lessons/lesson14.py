# import os
# import cv2 

# imgs = os.listdir('lesson14/manual_img')
# print(imgs)

# for img in imgs:
#     frame = cv2.imread('lesson14/manual_img/' + img)
#     frame = cv2.resize(frame, (500, 500))
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     frame = cv2.Canny(frame, 50, 200) # цей метод дозволяє визначити контури на зображенні
#     # frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
#     cv2.imshow('Frame', frame)
#     cv2.waitKey(1000)



#File System 2
# методи для роботи з файлами

# with open('lesson14/test.txt', 'w') as fl:
#     fl.write('Hello world')
    
# with open('lesson14/test.txt', 'r') as fl:
#     print(fl.read())

# with open('lesson14/test.txt', 'a') as fl:
#     fl.write('\nHello world')
    
# Функції для читання файлів
# .read() - читає весь файл
# .read(10) - читає 10 символів
# .readline() - читає один рядок
# .readlines() - читає всі рядки і повертає список рядків
# .readlines(10) - читає 10 рядків і повертає список рядків

#.seek() - переміщує курсор в файлі на позицію, яка вказана в аргументі
#.tell() - повертає поточну позицію курсора в файлі

# with open('lesson14/test.txt', 'r') as fl:
    # print(fl.read())
    # print('='*50)
    # fl.seek(150)
    # print(fl.read())
    # print(fl.read(10))
    # print(fl.tell())
    # print(fl.read(10))
    # print(fl.tell())
    # print(  fl.read(10).upper()  )
    # print(  fl.read(50).upper()  )
    # print(  fl.read(100).upper()  )
    
    # print(fl.tell())
    # print(fl.readline())
    # print('='*50)
    # print(fl.readline())
    # print('='*50)
    # print(fl.readline())
    # print('='*50)
    # print(fl.readline())
    # print('='*50)
    
    # print(fl.readlines())
    
    # print( fl.read().split()  )
    
    
# Функції для запису в файл
# .write(str) - записує в файл
# .writelines(list[str]) - записує список рядків в файл
# .writelines(str) - записує список рядків в файл

# names = ['Vasya', 'Petya', 'Kolya', 'Olya', 'Ira', 'Vika']


# with open('lesson14/test.txt', 'w') as fl:
#     fl.write('Hello world\n') 

   
#     fl.writelines(['Hello world2\n', 'Hello world3\n'])
#     fl.writelines('Hello world4\n')
#     names = '\n'.join(names)
#     fl.writelines(names)



#ТИПІЧНІ ПОМіЛКИ
# 1. Підрахуваємо кількість слів в тексті
# 2. Підрахуваємо кількість рядків в тексті
# 3. Підрахуваємо кількість символів в тексті


with open('lesson14/test.txt', 'r') as fl:
    all_text = fl.read()
    
    # count_words = len(all_text.split())
    # print('Кількість слів: ', count_words)
     
    words = all_text.split() # список слів
    
    words_without_symbols = [] # список слів без символів
    for word in words: # проходимо по кожному слову
        clear_word = [] # список для зберігання символів слова
        for symbol in word: # проходимо по кожному символу слова
            if symbol.isalpha():# перевіряємо чи символ є буквою
                clear_word.append(symbol)# якщо символ є буквою, то додаємо його в список
        if clear_word : # якщо довжина слова більша за 1, то додаємо слово в список слів без символів
            words_without_symbols.append(''.join(clear_word))# додаємо слово в список слів без символів
            
    print(words_without_symbols)
    print('Кількість слів: ', len(words_without_symbols))
    
    
    print('Кількість рядків: ', len(all_text.split('\n')))
    
    print('Кількість символів: ', len(all_text))
    # 4. Підрахуваємо кількість cлів, довжина яких парна
    count_words = 0
    for word in words_without_symbols:
        if len(word) % 2 == 0:
            count_words += 1
    print('Кількість слів, довжина яких парна: ', count_words)
    print('Кількість слів, довжина яких непарна: ', len(words_without_symbols) - count_words)


# 5. Отримати від користувача назву файлу та вивести на екран вміст файлу з номерами рядків



# JSON
# JSON - JavaScript Object Notation