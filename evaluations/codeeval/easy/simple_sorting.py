#!/usr/bin/env python
#-*- coding utf-8 -*-


import sys
import traceback


if __name__ == "__main__":

    arg = sys.argv[1]
    try:
        with open(arg, "r") as f:
            for line in f:
                splitted = line.strip().split()
                if splitted:
                    print(" ".join(sorted(splitted, key=float)))

    except Exception:
        print(traceback.format_exc())
