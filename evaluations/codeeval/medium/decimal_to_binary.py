#!/usr/bin/env python
#-*- coding:utf-8 -*-


import traceback
import sys


def dec_to_base(i, base):
    """Converts decimal to 'base', even if 'base' is negative"""
    bin_stack = []
    while i != 0:
        i, rem = divmod(i, base)
        if rem < 0:
            i, rem = i + 1, rem + abs(base) 
        bin_stack.append(str(rem))
    bin_stack.reverse()
    if not bin_stack:
        bin_stack.append("0")
    return bin_stack


if __name__ == "__main__":

    '''base = 2
    arg = sys.argv[1]
    try:
        with open(arg, "r") as f:
            for line in f:
                if line.strip():
                    binary = dec_to_base(int(line), base)
                    print("".join(binary))
    except IOError:
        print(traceback.format_exc())'''

    arg = sys.argv[1]
    try:
        with open(arg, "r") as f:
            for line in f:
                if line.strip():
                    #print(bin(int(line))[2:])
                    print("{0:b}".format(int(line)))
    except IOError:
        print(traceback.format_exc())

