#!/usr/bin/env python
#-*- coding: utf-8 -*-


import heapq
import traceback
import sys


if __name__ == "__main__":

    arg = sys.argv[1]
    heap = []
    try:
        with open(arg, "r") as f:
            nlines = int(f.readline())
            for line in f:
                if line.strip():
                    heapq.heappush(heap, (len(line), line.strip()))
    except IOError:
        print(traceback.format_exc())

    nlargest = heapq.nlargest(nlines, heap)
    for elem in nlargest:
        print(elem[1])

