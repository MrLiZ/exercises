#!/usr/bin/env python
#-*- coding:utf-8 -*-


import argparse
import traceback


def parser():
    """"""
    parser = argparse.ArgumentParser(description="Fizz Buzz")
    parser.add_argument("input_file", type=str, help="Config file to load")
    return parser.parse_args()


def fizz_buzz(A, B, N):
    """"""
    result = []
    for i in xrange(1, N + 1):
        #if i != 0 and i % A == 0 and i % B == 0:
        a_res = i % A
        b_res = i % B
        if a_res == 0 and b_res == 0:
            result.append("FB")
        elif a_res == 0:
            result.append("F")
        elif b_res == 0:
            result.append("B")
        else:
            result.append(i)
    return result


if __name__ == "__main__":

    args = parser()
    try:
        with open(args.input_file, "r") as f:
            for line in f:
                params = map(int, line.split())
                #params = [int(param) for param in line.split()]
                serie = fizz_buzz(*params)
                print(" ".join(map(str, serie)))
    except IOError as err:
        print(traceback.format_exc())
