#!/usr/bin/env python

'''
In base −2, integers are represented by sequences of bits in the following way. Sequence B of N bits represents the number: sum{ B[i]*(−2)i for i = 0..N−1 }. The empty sequence represents 0.

Note that such a representation is suitable for both positive and negative integers.

Write a function:

    def solution(A, B) 

that, given two zero-indexed arrays of bits:

        A of length M, containing a sequence representing some integer X, and
        B of length N, containing a sequence representing some integer Y,

returns the shortest sequence of bits representing X + Y.

The sequence should be returned as:

        a structure Results (in C), or
        a vector of integers (in C++), or
        a record Results (in Pascal), or
        an array of integers (in any other programming language).

For example, given A = [0,1,1,0,0,1,0,1,1,1,0,1,0,1,1] (X = 5730) and B = [0,0,1,0,0,1,1,1,1,1,0,1] (Y = −2396), the function should return [0,1,0,1,1,0,0,0,1,0,1,1,1] (X + Y = 3334).

Assume that:

        M and N are integers within the range [0..100,000];
        each element of array A is an integer that can have one of the following values: 0, 1;
        each element of array B is an integer that can have one of the following values: 0, 1.

Complexity:

        expected worst-case time complexity is O(M+N);
        expected worst-case space complexity is O(M+N), beyond input storage (not counting the storage required for input arguments).

Elements of input arrays can be modified.
'''


def negabinary(i, mod):
    bin_stack = []
    while i != 0:
        i, rem = divmod(i, mod)
        if rem < 0:
            i, rem = i + 1, rem + abs(mod) 
        bin_stack.append(rem)
    return bin_stack


def to_dec(bin_num, base):
    result = 0
    for i, elem in enumerate(bin_num):
        result += elem * (base)**i
    return result


def solution(A, B):
    """"""
    results = {
        -1: (1, 1),
        0: (0, 0),
        1: (1, 0),
        2: (0, -1),
        3: (1, -1)
    }
    carry = 0
    result = []
    for a, b in zip(A, B):
        num = int(a or 0) + int(b or 0) + carry
        bit, carry = results[num]
        result.append(bit)
    if carry:
        result.append(results[carry][0])
    return result


if __name__ == "__main__":

    A = 5730
    B = -2396
    base = -2
    bin_a = negabinary(A, base)
    bin_b = negabinary(B, base)
    bin_c = solution(bin_a, bin_b)
    print(bin_c, to_dec(bin_c, base))
    #C = [0,1,0,1,1,0,0,0,1,0,1,1,1] 3334 
