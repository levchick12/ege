from itertools import *

ans = 0
for val in product('вишня', repeat = 6):
    val = ''.join(val)
    if val.count('в') <= 1 and val[0] not in 'ш' and val[-1] not in 'ия': ans += 1
print(ans)