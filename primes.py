from functools import cache
from math import sqrt
import itertools as it

isprime = cache(lambda n: n != 1 and all(n % x for x in range(2, n) if x**2 <= n))

def sieve(n):
    mask = [True] * n
    primes = list(filter(isprime, range(2, int(sqrt(n)) + 1)))
    for prime in primes:
        mask[::prime] = len(mask[::prime]) * [False]
    return primes + list(it.compress(range(n), mask))[1:]
