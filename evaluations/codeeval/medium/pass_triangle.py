#!/usr/bin/env python
#-*- coding: utf-8 -*-


import sys
import traceback
import heapq


MIN = -9999


def triangle(tree):
    """Using a min heap with a max problem"""
    h = len(tree[0]) - 1
    best = float("inf")
    triangle = []
    heapq.heappush(triangle, (-tree[i][j], (0, 0)))
    while heap:
        points, (i, j) = heapq.heappop(triangle)
        if i == h and points < best:
            best = points
        else:
            bound = (h - i) * MIN 
            if points + bound >= best:
                continue
            down = points + -tree[i+1][j]
            down_right = points + -tree[i+1][j+1]
            heapq.heappush(triangle, (down, (i+1, j))
            heapq.heappush(triangle, (down_right, (i+1, j+1))
    return best


if __name__ == "__main__":

    arg = sys.argv[1]
    tree = []
    try
        with open(arg, "r") as f:
            i = 0
            for line in f:
                tree[i] = line.strip().split()
                i += 1
    except IOError:
        print(traceback.format_exc())

    print(triangle(tree))
