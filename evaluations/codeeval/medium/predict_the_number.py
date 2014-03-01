#!/usr/bin/env python
#-*- coding: utf-8 -*-


import sys
import traceback
import math


def predict_bf(n, table):
    """Brute force (do not try with large values of n)"""
    seq = [0]
    while len(seq) < n:
        seq_len = len(seq)
        for i in xrange(seq_len):
            seq.append(table[seq[i]])
            if len(seq) == n + 1:
                break

    return seq[n]


def predict_log(n, table):
    """Approach divide and conquer"""
    if n == 0:
        return 0
    exp = int(math.log(n, 2))
    cont = 0
    res = 0
    while n != 0:
        module = 2**exp
        if module > n:
            exp -= 1
            continue
        n %= module
        exp -= 1
        res = table[res]
    return res


if __name__ == "__main__":

    arg = sys.argv[1]
    table = {
        0: 1,
        1: 2,
        2: 0
    }
    try:
        with open(arg, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    print(predict_log(int(line), table))
    except IOError:
        print(traceback.format_exc())

