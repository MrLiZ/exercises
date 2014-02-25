#!/usr/bin/env python
#-*- coding: utf-8 -*-


import sys
import traceback


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


def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    primes = gen_primes()
    d = primes.next()
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = primes.next() 
        if d*d > n:
            if n > 1:
                factors.append(n)
            break
    return factors


if __name__ == "__main__":

    # Constraints: 
    ## 0 <= X <= 2147483647
    ## 1 <= N <= 100 
    # SOLUTION: the number of integer solutions of k = x^2 + y^2 is:
    # the number of prime divisors of k which are equal to 1 mod 4 or
    # zero if there is a prime divisor equal to 3 mod 4.
    # 1. All prime numbers up to sqrt(max(X)) = sqrt(2147483647) = 46341
    # 2. Compute the prime divisors of k (using sieve, testing up to sqrt(k))
    # Count the ones which are equal to 1 mod 4 and sum. Multiply answer by 4
    arg = sys.argv[1]
    try:
        with open(arg, "r") as f:
            num_sols = int(f.readline())
            for i, line in enumerate(f):
                k = int(line.strip())
                if k in (0, 1):
                    print("1")
                    continue
                factors = prime_factors(k)
                count = 0
                for factor in factors:
                    if factor % 4 == 3:
                        count = 0
                        break
                    if factor % 4 == 1:
                        count += 1
                print(str(count))
                if i + 1 == num_sols:
                    break

    except IOError:
        print(traceback.format_exc())

