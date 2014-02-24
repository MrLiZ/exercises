#!/usr/bin/env python
#-*- coding:utf-8 -*-


import sys
import traceback


if __name__ == "__main__":

    arg = sys.argv[1]
    try:
        with open(arg, "r") as f:
            for line in f:
                splitted = line.strip().split()
                if splitted:
                    length = len(splitted)
                    pos = int(splitted[length - 1])
                    if pos <= length - 1:
                        print(splitted[length - pos - 1])
    except IOError:
        print(traceback.format_exc())
