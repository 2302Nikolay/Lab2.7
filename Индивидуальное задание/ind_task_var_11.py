#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

if __name__ == '__main__':

    # Множества
    u = set("abcdefghiklmnopqrstuvwxyz")
    a = set("abhkor")
    b = set("bghls")
    c = set("klz")
    d = set("gjpquv")

    # Решение задачи
    x = (a & c) or b
    na = u - a
    nb = u - b
    y = (na & b) - (c or d)

    """""
    x = (a.intersection(c)).union(b)
    na = u.difference(a)
    nb = u.difference(b)
    y = (na.intersection(b)).difference(c.union(d))
    """""
    # Вывод результата
    print("X = ", x)
    print("Y = ", y)
