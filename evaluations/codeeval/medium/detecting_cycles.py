#!/usr/bin/env python
#-*-- coding: utf-8 -*-


import sys
import traceback


def floyd(seq):
    """Floyd's cycle-finding algorithm adapted
       (http://en.wikipedia.org/wiki/Cycle_detection)"""
    print(seq)
    length = len(seq)
    if length == 1:
        return (-1, None)
    if length == 2:
        return (0, 1) if seq[0] == seq[1] else (-1, None)
        
    t = 1
    h = 2
    tortoise = seq[t]
    hare = seq[h]
    while tortoise != hare:
        t += 1
        tortoise = seq[t]
        h = h + 2 if h + 2 < length else length - 1
        hare = seq[h]
    print("{} {}".format(t, h))

    aux = h 
 
    mu = 0
    t = 0
    tortoise = seq[t]
    while tortoise != hare:
        t += 1
        tortoise = seq[t]
        h = h + 1 if h + 1 <= length else aux 
        hare = seq[h]
        mu += 1
    print("{} {}".format(t, h))
 
    lam = 1
    h = t + 1 if t + 1 < length else length
    hare = seq[h]
    while tortoise != hare:
        h = h + 1 if h + 1 < length else length
        hare = seq[h]
        lam += 1
    print("{} {}".format(t, h))

    return t, h


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
                    '''init, end = floyd(splitted)
                    if init != -1: 
                        print(" ".join(splitted[init:end]))'''
                    cycle = find_cycles(splitted)
                    if cycle:
                        print(" ".join(cycle))
    except IOError:
        print(traceback.format_exc())

