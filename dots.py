from num_to_img import *
import bit8.bw as bw
from primes import sieve
import itertools as it

i = iter(sieve(100000))
next(i)
l = nl_to_bl(i, iaef=map(lambda x: x + 1, it.accumulate(it.count(1))))
# l = nl_to_bl(range(1, 100000, 2))
# l = nl_to_bl(x**2 for x in range(0, 100))
scr = spiral(l)
bw.render(scr, False)

# 3d spiralifier
