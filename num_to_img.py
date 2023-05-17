import itertools as it
import operator as op

def wrap(_l, x, y):
    ans = []
    l = iter(_l)
    for i in range(y):
        ans.append([])
        for j in range(x):
            try:   # Can probably factor this out
                ans[i].append(next(l))
            except StopIteration:
                ans[i].append(0)
    return ans

def nl_to_bl(nl, start=0, step=1, iaef=None):
    if iaef is None: iaef = it.count(start, step)
    'Number list to bit list'
    i = iter(nl)
    try:
        cur = next(i)
        for x in iaef:
            if x == cur:
                yield 1
                cur = next(i)
            else:
                yield 0
            while x > cur:
                cur = next(i)
    except StopIteration:
        return

def transpose(l):
    return list(zip(*l))

def rotate(l):
    return transpose(map(reversed, l))

def spiral(_l):    # When rotate is replaced with transpose, diagonal lines become straight
    "Spiralifies l. Imagine winding the list around a fixed point; that's this algorithm."
    l = iter(_l)
    ans = [[next(l)]]
    tl = 1    # Total length
    c = True
    d = 0     # Direction
    while c or pow(int(pow(tl, 0.5)), 2) != tl:
        N = len(ans)  # expected slice len
        new = list(it.islice(l, N))
        if N != len(new):
            new.extend((N - len(new)) * [0])
            c = False
        ans = rotate(list(x) + [y] for x, y in zip(ans, new))
        d = (d + 1) % 4
        tl += N
    return list(map(list, ans))

if __name__ == '__main__':
    import bit8
    import math
    bit8.render(spiral((int(math.atan(x) * 255),) * 3 for x in range(2, 1000)), False)
