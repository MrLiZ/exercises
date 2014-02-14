#!/usr/bin/env python

'''
Four integers A, B, C and D are given. A shuffle of them is any zero-indexed array S consisting of these four integers in some order. If all the given integers are unique, then there are 24 different shuffles of them.

The best shuffle of the given integers is any shuffle S of them such that the value of:

  F(S) = abs(S[0]-S[1]) + abs(S[1]-S[2]) + abs(S[2]-S[3])

is maximal.

Write a function:

    def solution(A, B, C, D) 

that, given four integers A, B, C and D, finds their best shuffle S and returns the value of F(S).

For example, consider the following integers:

  A = 5    B = 3    C = -1    D = 5

The best shuffle of them is as follows:

  S[0] =  5
  S[1] = -1
  S[2] =  5
  S[3] =  3

and the result is F(S) = 14.

Assume that:

        A, B, C and D are integers within the range [−1,000,000..1,000,000].

Complexity:

        expected worst-case time complexity is O(1);
        expected worst-case space complexity is O(1).

'''


import itertools


def solution(A, B, C, D):
    """"""
    permutator = itertools.permutations([A, B, C, D])
    max_f = float("-inf")
    max_perm = []
    for perm in permutator:
        f = (abs(perm[0] - perm[1]) + abs(perm[1] - perm[2]) 
             + abs(perm[2] - perm[3]))
        if f > max_f:
            max_f = f
            max_perm = perm
    return max_perm, max_f


if __name__ == "__main__":

    A, B, C, D = 5, 3, -1, 5
    print(solution(A, B, C, D))
