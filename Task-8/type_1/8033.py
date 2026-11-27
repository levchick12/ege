from itertools import *

ans = []
alph = sorted('январь')
for pos, val in enumerate(product(alph, repeat=5), start =1):
    val = ''.join(val)
    if val[0] not in 'я' and val.count('ь') <= 1 and val[2] not in 'я' and val[4] not in 'я':
        ans.append([pos, val])
print(max(ans))