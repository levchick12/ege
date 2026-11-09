from math import ceil, log2
L = 248
for N in range(1,10000):
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if I * 75600 > 16 * 2 ** 20:
        print(N)
        break


