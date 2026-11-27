from itertools import *

ans = []
alph = sorted('аворт')

for res, val in enumerate(product(alph, repeat = 6), start = 1):
    val = ''.join(val)
    if val in 'ворота':
        ans.append([res, val])
print(ans)