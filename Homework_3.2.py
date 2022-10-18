# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


def multiply_list_elem(num_list):
    even_len = 0
    new_list = []
    if not len(num_list) % 2 == 0:
        even_len = int((len(num_list) +1) / 2)
    else:
        even_len = int(len(num_list) / 2)
    for i in range(0, even_len):
        new_list.append(num_list[i] * (num_list[len(num_list) - i - 1]))
    return new_list

num_list_1 = [2, 3, 4, 5, 6]
num_list_2 = [2, 3, 5, 6]
new_list = multiply_list_elem(num_list_1)
print(f'{num_list_1} => {new_list}')







