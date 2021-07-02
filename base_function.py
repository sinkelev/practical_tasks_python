import re
import os
import time
import datetime


def delete_a(s):
    """
    В строке удалить все буквы "а"
    и подсчитать количество удаленных символов
    """

    print(f"Строка {s} без символов 'а': {s.replace('a', '')}")
    print(f"Удалено букв 'а': {s.count('a')} ")


def check_num(phone_numbers):
    """Проверить, что номера телефонов состоят только из цифр."""
    template = '^(8|\+7)[\- ]?(\d{3}?[\- ]?)?[\d\- ]{7,10}$'
    for phone in phone_numbers:
        if re.match(template, phone):
            print(phone + ' True')
        else:
            print(phone + ' False')


def name_file(path):
    """Имя файла без расширения из строки"""
    basename = os.path.basename(path)
    basename_without_extension = basename.split('.')[0]
    print(basename_without_extension)


def func_time(func):
    """
    Декоратор, который подсчитывает
    и выводит сколько времени выполняется функция
    """

    def wrapped(*args):
        start_time = time.perf_counter()
        func(*args)
        time_work = time.perf_counter() - start_time
        result = datetime.timedelta(seconds=time_work).total_seconds()
        print(f"Функция {func.__name__}"
              f"выполнялась {format(result, '.5f')} сек")

    return wrapped


@func_time
def change_max_min(num):
    """Меняет местами самый большой и самый маленький элементы списка"""
    maximum = max(num)
    minimum = min(num)
    for i in range(len(num)):
        if num[i] == maximum:
            num[i] = minimum
        elif num[i] == minimum:
            num[i] = maximum
    print(num)


def sort_dict(price):
    """Найти ТОП-2 самых дорогих товаров из списка словарей"""
    sort_price = sorted(price, key=lambda k: k["цена"], reverse=True)
    print(sort_price[0:2])


def lucky_tickets():
    """
    Функция, которая подсчитывает
    количество счастливых шестизначных билетов
    """

    i = 0
    for num in range(1000000):
        st = str(num)
        st = '0' * (6 - len(st)) + st
        if int(st[0]) + int(st[1]) + int(st[2]) == \
                int(st[3]) + int(st[4]) + int(st[5]):
            i += 1
    print(i)


# delete_a('123a456a7a')
check_num(['8-999-777-1111',
           '+7 999 333 2222',
           '+7 999-555-11-11',
           'absc',
           '+7'])
# name_file('C:\\development\\inside\\test-project_management\\inside\\myfile.txt')
# change_max_min([2, 2, 1, 4, 5, 6])
# lucky_tickets()
price = [
    {"наименование": "Спички", "цена": 1},
    {"наименование": "Сок", "цена": 60},
    {"наименование": "Лук", "цена": 37},
    {"наименование": "Горох", "цена": 50},
]
sort_dict(price)
