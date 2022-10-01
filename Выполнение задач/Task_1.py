#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

if __name__ == '__main__':
    str_in = input("Введите строку: ").lower()
    a = set(str_in)
    u = set("aeiouyаоуыэеёиюяи")
    gl = a.intersection(u)
    print("Количество гласных букв в строке: ", len(gl))
