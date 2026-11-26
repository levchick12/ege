from itertools import *

ans = []
alpf = sorted("ТЕОРИЯ")

for pos, val in enumerate(product(alpf, repeat = 6), start =1):
    val = ''.join(val)
    if pos % 2 == 1 and val.count('И') == 2 and (val[0] not in 'ЯТР'):
        ans.append([pos, val])
print(max(ans))