# import numpy as np
from functools import cache
from num_to_img import spiral
import bit8
import colorsys
import math
from complex_utils import add_n

to255 = lambda *a: tuple(int(x*255) for x in a)

def hsv_to_rgb(h, s, v):
    return to255(*colorsys.hsv_to_rgb(h,s,v))

@cache
def is_prime(n):
    if n == 2: return True
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

@cache
def totient(n):
    if n == 0: return 0
    if n == 1: return 1
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            if (n // i) % i == 0:
                return i * totient(n // i)
            return (i - 1) * totient(n // i)
    raise ValueError(n)


# For odd totients, interesting corner shapes appear
# l = (1 - totient(x) / x for x in range(1, 10000, 2))
from time import sleep
for x in range(1, 2):
    # if is_prime(x):
    if True:
        l = (math.atan(totient(x)) * 2/math.pi for x in range(0, 10000 * x, x))
        scr = spiral((int(x * 255),) * 3 for x in l)
        bit8.render(add_n(scr, x), True)
        # sleep(3)
