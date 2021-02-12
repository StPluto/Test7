#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    #   В списке, состоящем из целых элементов, вычислить номер максимального элемента списка;
    a = tuple(map(int, input("Введите кортеж: ").split()))
    if not a:
        print("Заданный кортеж пуст", file=sys.stderr)
        exit(1)
    a_max = a[0]
    position = 0
    #   Номер максимального элемента кортежа
    for i, item in enumerate(a):
        if item > a_max:
            position, a_max = i, item
    print("Номер максимального элемента кортежа:", position)