from itertools import *

ans = []
alph = sorted('авлор')
for pos,val in enumerate(product(alph, repeat = 4), start = 1):
    val = ''.join(val)
    if val[0] in 'л':
        ans.append([pos, val])
print(min(ans))