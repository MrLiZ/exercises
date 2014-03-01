#!/usr/bin/env python
#-*- coding: utf-8 -*-


import sys
import traceback


if __name__ == "__main__":

    arg = sys.argv[1]
    try:
        with open(arg, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                num, p1, p2 = map(int, line.split(","))
                num_bin = bin(num)[:1:-1]
                print("true") if num_bin[p1-1] == num_bin[p2-1] else "false"

    except IOError:
        print(traceback.format_exc())
    except IndexError:
        print("false")
