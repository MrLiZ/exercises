#!/usr/bin/env python
#-*- coding:utf-8 -*-


'''Constraints:
    N is in range [0, 100]
    L is in range [10000, 30000]
    The number of test cases <= 40 
'''


import sys
import traceback


if __name__ == "__main__":

    arg = sys.argv[1]
    try:
        with open(arg, "r") as f:
            for line in f:
                results = {}
                splitted = line.strip().split(",")
                found = False
                for num in splitted:
                    results[num] = 1 if not num in results else results[num]+1
                    if results[num] > len(splitted)/2:
                        found = True
                        print(num)
                        break
                if not found:
                    print("None")

    except IOError:
        print(traceback.format_exc())

