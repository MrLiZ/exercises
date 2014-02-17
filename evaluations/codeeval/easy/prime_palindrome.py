#!/usr/bin/env python
#-*- coding: utf-8 -*-


import math


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


if __name__ == "__main__":

    N = 1000
    for i in xrange(N, 1, -1):
        prime_i = str(i)
        if prime_i == prime_i[::-1] and is_prime(i):
            print(i)
            break
