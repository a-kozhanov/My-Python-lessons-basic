# coding=utf-8

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.


list_fruits_1 = ["яблоко", "банан", "киви", "арбуз", "груша", "яблоко", "яблоко", "яблоко", "картошка"]
list_fruits_2 = ["яблоко", "банан", "киви", "арбуз", "дыня", "гранат"]


for item in list_fruits_2:
    while item in list_fruits_1:
        list_fruits_1.remove(item)

print(list_fruits_1)
