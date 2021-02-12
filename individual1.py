# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Составить программу, выдающую индексы заданного элемента или сообщающую, что
    # такого элемента в списке нет.
    a = tuple(map(int, input("Введите кортеж: ").split()))
    m = int(input("Введите элемент: "))
    z = []
    for item in range(len(a)):
        if a[item] == m:
            z.append(item)

    if len(z) == 0:
        print("Такого элемента нет в кортеже.")
    else:
        print("Индексы заданного элемента:", z)