#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

if __name__ == '__main__':

    # Введение двух строк
    str_1 = input("Введите первую строку: ")
    str_2 = input("Введите вторую строку: ")
    # Преобразование строки в множество
    frst_s = set(str_1)
    sec_s = set(str_2)

    # Нахождение общих символов
    a = frst_s.intersection(sec_s)
    print("Общие символы:", a)
