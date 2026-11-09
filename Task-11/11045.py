from math import log2, ceil
L = 105
for N in range(1,10000):
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if 65536 * I >= 7 * 2 ** 20:
        print(N)
        break
