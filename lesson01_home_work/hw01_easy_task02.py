# coding=utf-8

__author__ = 'Ваши Ф.И.О.'

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!


a = input('Введите значение a: ')
b = input('Введите значение b: ')

# a, b = b, a
t = a
a = b
b = t

print("a =", a, "b =", b)
