# coding=utf-8

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

list_numbers = [2, 15, 9, 20, 7, 12, 1, 23]
new_list = []

for item in list_numbers:
    if item % 2 == 0:
        new_list.append(item * 2)
        print(item)
    else:
        new_list.append(item / 4)

print(new_list)
