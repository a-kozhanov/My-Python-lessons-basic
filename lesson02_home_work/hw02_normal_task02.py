# coding=utf-8

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

# locale-gen ru_RU.UTF-8

import calendar
import locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
locale.setlocale(locale.LC_ALL, ('ru_RU', 'UTF-8'))

for name in calendar.month_name:
    print(name.capitalize())
