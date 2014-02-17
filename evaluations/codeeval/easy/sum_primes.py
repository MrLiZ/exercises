#!/usr/bin/env python
#-*- coding: utf-8 -*-

def is_prime(n):
    """"""
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

    i = 0 
    total = 0
    N = 1000
    primes = gen_primes()

    while i < N:
        total += primes.next()
        i += 1
    print(total)
