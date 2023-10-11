# Homework 8 - Vladislav

print("type your numbers or type end to stop\n")
input_list = []

typing = True
while typing == True:
    input_number = input("enter a number:")
    if input_number.isdigit() == True:
        input_list.append(int(input_number))
    elif input_number == 'end':
        break
    else:
        print("invalid input")


# task 1 - index


index_list = [value for index, value in enumerate(input_list) if index % 2 == 0]
print("\ntask 1(even index):", index_list)


# task 2 - sum


total = 0
[total := total + element for element in input_list]
print("\ntask 2(sum):", total)


# task 3 - sum 2


total_even = 0
total_odd = 0

[total_even := total_even + element for element in input_list if element % 2 == 0]

[total_odd := total_odd + element for element in input_list if element % 2 != 0]

print("\ntask 3(even/odd sum): odd={0}, even={1}".format(total_odd, total_even))


# task 4 - biggest element


biggest_list = [(index, element) for index, element in enumerate(input_list) if max(input_list) == element]

print("\ntask 4(biggest element)\nfirst value is index, second is value:\n\t", biggest_list[0])