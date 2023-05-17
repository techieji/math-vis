from complex_utils import plot_f
from time import sleep
import numpy as np
from sympy import *
from functools import reduce
from operator import mul
import itertools as it

def basic_polynominals():
    for n in range(0, 10):
        plot_f(lambda x: x**n - 1, zoom=0.05, bound=2, move_c=True)
        sleep(3)

def _cyclotomic(n):
    def f(x):
        prod = 1
        for k in range(1, n + 1):
            if np.gcd(k, n) == 1:
                prod *= x - np.e**(2j * np.pi * k/n)   # Copied off of wikipedia
        return prod
    return f

x = symbols('x')

def cyclotomic(n):
    s = reduce(mul, (x - E**(I*2*pi*r/n) for r in range(1, n) if np.gcd(r, n) == 1), 1)
    return s

from primes import sieve

p1, p2 = it.tee(sieve(15))
sp = sorted(x * y for x in p1 for y in p2)

def cyclotomic_simul():
    for i in sp:
        s = cyclotomic(i)
        d = Derivative(s).doit()
        if True:
            plot_f(lambdify(x, s, 'numpy'), lambdify(x, d, 'numpy'), zoom=0.05, bound=2, center=(0, 0), move_c=True, n=i)
            sleep(4)

basic_polynominals()
