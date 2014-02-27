#!/usr/bin/env python
#-*- coding: utf-8 -*-


import sys
import traceback


def perfect_squares(x):
    """"""
    i = 0
    j = int(1 + x ** 0.5)
    count = 0
    #sols = []

    while i <= j:
        solution = i**2 + j**2
        if solution == x:
            #sols.append((i, j))
            count += 1
            i += 1
            j -= 1
        elif solution < x:
            i += 1
        else:
            j -= 1
    return count #, sols


if __name__ == "__main__":

    arg = sys.argv[1]
    try:
        with open(arg, "r") as f:
            num_sols = int(f.readline())
            for i, line in enumerate(f):
                if i == num_sols:
                    break

                k = int(line.strip())
                print(perfect_squares(k))
    except IOError:
        print(traceback.format_exc())

