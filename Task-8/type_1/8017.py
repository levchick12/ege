from itertools import *

ans = []
alph = sorted('аклмня')
for res, val in enumerate(product(alph, repeat = 5), start = 1):
    val = ''.join(val)
    if val [:2] in 'км':
        ans.append([res, val])
print(min(ans))