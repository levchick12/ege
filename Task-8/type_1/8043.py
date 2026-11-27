from itertools import *

ans = []
alph = sorted('алгоритм')

for pos, val in enumerate(product(alph, repeat = 5), start = 1 ):
    val = ''.join(val)
    if pos % 2 == 0 and val[0] not in 'аг' and val.count('р') >= 2:
        ans.append([pos,val])
print(min(ans))