#!/usr/bin/env python
#-*- coding: utf-8 -*-

def solution(A):
    """"""
    if not A:
        return -1
    else:
        tot = sum(A)
        acum = 0
        for i, elem in enumerate(A):
            tot -= elem
            if tot == acum:
                return i
            acum += elem
        return -1


if __name__ == "__main__":

    A = [-7, 1, 5, 2, -4, 3, 0]
    print(solution(A))
