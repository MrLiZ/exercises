#!/usr/local/bin python
#-*- coding: utf-8 -*-


import sys
import traceback


def longest_common_subseq(a, b):
    """"""
    length_a = len(a) + 1
    length_b = len(b) + 1
    matrix = [[set([]) for i in xrange(length_b)] for j in xrange(length_a)]
    for i in xrange(1, length_a):
        for j in xrange(1, length_b):
            if a[i - 1] == b[j - 1]:
                diag = matrix[i - 1][j - 1]
                if not diag:
                    matrix[i][j].add(a[i - 1])
                else:
                    for elem in diag:
                        matrix[i][j].add(elem + a[i - 1])
            else:
                up = matrix[i - 1][j]
                left = matrix[i][j - 1]
                up_len = len(iter(up).next()) if up else 0
                left_len = len(iter(left).next()) if left else 0
                if up_len > left_len:
                    matrix[i][j].update(up) 
                elif up_len < left_len:
                    matrix[i][j].update(left) 
                else:
                    matrix[i][j].update(up) 
                    matrix[i][j].update(left) 

    return matrix[len(a)][len(b)]

if __name__ == "__main__":

    arg = sys.argv[1]
    try:
        with open(arg, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    splitted = line.split(";")
                    res = longest_common_subseq(*splitted)
                    if res:
                        print("".join(res))
    except IOError:
        print(traceback.format_exc())
