from itertools import *

ans = []
alph = sorted('победа')
for pos, val in enumerate(product(alph, repeat=6), start =1):
    val = ''.join(val)
    if pos % 2 == 0 and val[0] in 'о' and len(set(val)) == 6:
        ans.append(pos)
print(max(set(ans)))