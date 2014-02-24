#!/usr/bin/env python
#-*-- coding: utf-8 -*-


import sys
import traceback


def floyd(seq):
    """Floyd's cycle-finding algorithm adapted
       (http://en.wikipedia.org/wiki/Cycle_detection)"""
    if len(seq) == 1:
        return -1, None
    if len(seq) == 2:
        return (0, 1) if seq[0] == seq[1] else (-1, None)
        
    t = 1
    h = 2
    length = len(seq) - 1
    tortoise = seq[t]
    hare = seq[h]
    while tortoise != hare:
        t += 1
        tortoise = seq[t]
        h = min(h + 2, length)
        hare = seq[h]
 
    mu = 0
    t = 0
    tortoise = seq[t]
    while tortoise != hare:
        t += 1
        tortoise = seq[t]
        h = min(h + 1, length)
        hare = seq[h]
        mu += 1
 
    lam = 1
    h = min(t + 1, length)
    hare = seq[h]
    while tortoise != hare:
        h = min(h + 1, length)
        hare = seq[h]
        lam += 1

    return (-1, None) if t == h else (mu, lam)


if __name__ == "__main__":

    arg = sys.argv[1]
    try:
        with open(arg, "r") as f:
            for line in f:
                splitted = line.strip().split()
                if splitted:
                    init, length = floyd(splitted)
                    if init != -1: 
                        print(" ".join(splitted[init:init+length]))
                    else:
                        print("No cycles")
    except IOError:
        print(traceback.format_exc())

