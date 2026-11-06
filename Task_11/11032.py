from math import log2, ceil
for L in range(1,100000):
    N = 10 + 52 + 963
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if I * 2000 <= 693 * 2 ** 10:
        print(L)
