import numpy as np
import colorsys
import bit8
from functools import reduce

hsv_to_rgb = np.vectorize(colorsys.hsv_to_rgb)

complex_to_color = lambda z: [(x*255).astype(int) for x in hsv_to_rgb(np.angle(z, deg=True) / 360 + 0.5, 1, np.minimum(1, 0.5*np.log(np.abs(z) + 1)))]

NUMBERS = bit8.bsl.parse_file('numbers.scr')

def add_n(scr, n):
    scr = bit8.utils.adjoin(scr, bit8.utils.solid(6, 10, 'n'))
    for x in str(n):
        scr = bit8.utils.adjoin(scr, bit8.utils.recolor(NUMBERS[x], '# ', 'wn'), buffer=1)
    return scr

def plot_f(*fs, zoom=0.25, bound=5, center=(0,0), move_c=False, n=None):
    a = bound
    scrs = [[[tuple(complex_to_color(f(complex(x, y)))) for x in np.arange(-a, a, zoom) + center[0]] for y in np.arange(-a, a, zoom) + center[1]] for f in fs]
    scr = reduce(lambda a, b: bit8.utils.adjoin(a, b, buffer=10), scrs)
    if n is not None:
        scr = add_n(scr, n)
        # scr = bit8.utils.adjoin(scr, bit8.utils.solid(6, 10, 'n'))
        # for x in str(n):
        #     scr = bit8.utils.adjoin(scr, bit8.utils.recolor(NUMBERS[x], '# ', 'wn'), buffer=1)
    bit8.render(scr, move_c)
