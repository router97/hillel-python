# Homework 11 - Vladislav


from random import randint

list1 = [randint(0, 99) for i in range(randint(1, 9))]
list2 = [randint(0, 99) for i in range(randint(1, 9))]

print("list 1: {0}\nlist 2: {1}".format(list1, list2))


# task 1 - biggest number


def find_biggest(list):
    tmp = 0
    for index in range(len(list)-1):
        if list[index+1] < list[index]:
            tmp = list[index]
            list[index] = list[index+1]
            list[index+1] = tmp
          
find_biggest(list1)
find_biggest(list2)
     
biggest_number1 = list1[-1]
biggest_number2 = list2[-1]


print("\ntask 1(biggest number)(list1): {0}\ntask 1(biggest number)(list2): {1}".format(biggest_number1, biggest_number2))


# task 2 - similarities


def remove_copies(list):
    for i in range(len(list)+1):
        for index in range(len(list)):
            if index <= (len(list) - 2):
                if list[index+1] == list[index]:
                    list.remove(list[index])
                else:
                    continue
            else:
                break


def find_similarities(list):
    for element in list:
        for index in range(len(list)-1):
            
            if list[index+1] == list[index]:
                return True
            else:
                continue

def find_similarities_main(list1, list2):

    list1 = sorted(list1)
    list2 = sorted(list2)
    
    remove_copies(list1)
    remove_copies(list2)
    
    list1.extend(list2)
    list1 = sorted(list1)
    
    if find_similarities(list1) == True:
        return True
    else:
        return False


if find_similarities_main(list1, list2) == True:
    print("\ntask 2(similarities): True")
    
else:
    print("\ntask 2(similarities): False")


# можно и так
def find_similar(list):   
    numbers_set = set()
    for it in list:
       if (it in numbers_set):
           return True
       numbers_set.add(it)
    return False