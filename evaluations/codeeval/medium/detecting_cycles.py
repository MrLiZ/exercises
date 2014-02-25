#!/usr/bin/env python
#-*-- coding: utf-8 -*-


import sys
import traceback


def find_cycles(seq):
    """"""
    aux = {}
    for i, elem in enumerate(seq):
        if elem not in aux:
            aux[elem] = i
        else:
            init = aux[elem]
            return seq[init:i]
    return []


if __name__ == "__main__":

    arg = sys.argv[1]
    try:
        with open(arg, "r") as f:
            for line in f:
                splitted = line.strip().split()
                if splitted:
                    cycle = find_cycles(splitted)
                    if cycle:
                        print(" ".join(cycle))
    except IOError:
        print(traceback.format_exc())

