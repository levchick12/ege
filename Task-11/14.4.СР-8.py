from math import ceil, log2
for L in range(1,10000):
    N = 10 + 52 + 972
    i = ceil(log2(N))
    I = ceil(i * L / 8)
    if 2048 * I < 172 * 2**10:
        print(L)