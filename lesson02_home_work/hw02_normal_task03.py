# coding=utf-8

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random

list_random_numbers = []

for i in range(10):
    list_random_numbers.append(random.randint(-100, 100))

print(list_random_numbers)
