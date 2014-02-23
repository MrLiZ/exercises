#!/usr/bin/env python
#-*- coding: utf-8 -*-


import timeit
import math


def sieve(n):
    "Return all primes <= n."
    np1 = n + 1
    s = range(np1) # leave off `list()` in Python 2
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in xrange(2, sqrtn + 1):
        if s[i]:
            s[i*i: np1: i] = [0] * len(xrange(i*i, np1, i))
    return filter(None, s)


def primes_Tim(prime, n):
    """Tim Peters solution"""
    primes = set(sieve(n))
    return True if prime in primes else False


def primes_Tony(n):
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


def gen_primes():
    """ Generate an infinite sequence of prime numbers"""
    D = {}  
    q = 2  
    while True:
        if q not in D:
            yield q        
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


if __name__ == "__main__":

    prime = 982451653
    '''n = 6000000
    tims_timer = timeit.Timer("primes_Tim({}, {})".format(prime, n),
                              "from __main__ import primes_Tim")
    tims = tims_timer.timeit(number=100)
    print("Tim's solution: {}".format(tims))'''
    tonys_timer = timeit.Timer("primes_Tony({})".format(prime),
                               "from __main__ import primes_Tony")
    tonys = tonys_timer.timeit(number=1000)
    print("Tony's solution: {}".format(tonys))



