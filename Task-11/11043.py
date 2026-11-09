from math import log2, ceil

N = 10 + 52 + 500
i = ceil(log2(N))
for L in range(1, 100000):
    I = ceil(L * i / 8)
    if I * 45877 > 49 * 2 ** 20:
        print(L)
        break