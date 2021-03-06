#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    #   В списке, состоящем из целых элементов, вычислить произведение элементов списка,
    #   расположенных между первым и вторым нулевыми элементами.
    a = tuple(map(int, input("Введите кортеж: ").split()))
    if not a:
        print("Заданный кортеж пуст", file=sys.stderr)
        exit(1)
    a_max = a[0]
    position = 0
    #   Произведение элементов кортежа, расположенных между первым и вторым нулевыми элементами.
    lst = []
    for i, item in enumerate(a):
        if item == 0:
            lst.append(i)
    x = lst[0] + 1
    y = lst[1]
    m = 1
    for item in a[x:y]:
        m *= item
    print("Произведение элементов кортежа, расположенных между первым и вторым нулевыми элементами равно:", m)