#!/usr/bin/env python
#-*- coding: utf-8 -*-


import sys
import traceback
import math
import bisect


def is_prime(n):
    """It utilizes the fact that primes > 4 are 1(mod 6) or 5(mod 6):
        Every prime number is either of the form 6k+ 1;6k+ 5, or 2;3.
        Indeed, there are no primes of the form 6k, since 2 is a proper 
        divisor of all such positive integers, the only prime of the 
        form 6k+ 2 is 2, the only prime of the form 6k+ 3 is 3, and
        there are no primes of the form 6k+ 4, since again 2 is a 
        proper divisor of all such positive integers. Since 2;3, no pi 
        divides N, this means that N must be a product of only primes 
        of the form 6k+ 1"""
    if n == 2 or n == 3:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False

    r = int(math.sqrt(n))
    f = 5
    while f <= r:
        if n % f == 0 or n % (f + 2) == 0:
            return False
        else:
            f += 6
    return True


def binary_search(a, x, lo=0, hi=None):
    """Uses bisect to search for the elements of a below x"""
    hi = hi if hi is not None else len(a)
    pos = bisect.bisect_left(a,x,lo,hi)
    return pos


def get_primes_below_n(n, last, primes):
    """"""
    if last > n:
        end = binary_search(primes, n)
        return primes[:end]
    else:
        #FIXME: 2?
        if last % 2 == 0:
            last += 1
        for i in xrange(last, n, 2):
            if is_prime(i):
                primes.append(i)

    return primes


if __name__ == "__main__":


    arg = sys.argv[1]
    primes = []
    last = 0
    try:
        with open(arg, "r") as f:
            for line in f:
                n = int(line)
                first_n_primes = get_primes_below_n(n, last, primes)
                print(str(first_n_primes))
                last = n

    except IOError:
        print(traceback.format_exc())

