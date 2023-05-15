from num_to_img import *
import bit8.bw as bw
from primes import sieve

# l = nl_to_bl(sieve(100000))
# l = nl_to_bl(range(1, 100000, 2))
l = nl_to_bl(x**2 for x in range(0, 100))
scr = spiral(l)
bw.render(scr, False)
