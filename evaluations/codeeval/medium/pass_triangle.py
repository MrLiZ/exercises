#!/usr/bin/env python
#-*- coding: utf-8 -*-


import sys
import traceback
import heapq


def triangle_bandb(tree):
    """Branch and bound approach (up to 34 rows)"""
    MIN = -9999 # maximization problem with min heap
    h = len(tree) - 1
    best = float("inf")
    heap = []
    heapq.heappush(heap, (-tree[0][0], 0, 0))
    while heap:
        points, i, j = heapq.heappop(heap)
        if i == h and points < best:
            best = points
        else:
            bound = (h - i) * MIN 
            if points + bound >= best:
                continue
            down = points + -tree[i+1][j]
            down_right = points + -tree[i+1][j+1]
            heapq.heappush(heap, (down, i+1, j))
            heapq.heappush(heap, (down_right, i+1, j+1))

    return -best


def triangle_dp(tree):
    """Dinamic programming approach"""
    h = len(tree)
    res = [0] * h
    res[h - 1] = tree[h - 1]
    for i in xrange(h - 2, -1, -1):
        row_length = len(tree[i])
        res[i] = [0] * row_length
        for j in xrange(row_length - 1, -1, -1):
            res[i][j] = tree[i][j] + max(res[i+1][j], res[i+1][j+1])

    return res[0][0] 


if __name__ == "__main__":

    arg = sys.argv[1]
    tree = []
    try:
        with open(arg, "r") as f:
            for line in f:
                tree.append(map(int, line.strip().split()))
                #tree.append([int(x) for x in line.strip().split()])
    except IOError:
        print(traceback.format_exc())

    print(triangle_dp(tree))
