from itertools import *

alph = sorted('цапля')
ans = []
for res, val in enumerate(product(alph, repeat = 5), start = 1):
    val = ''.join(val)
    if val.count('а') <= 1 and val.count('ц') == 2 and val.count('л') == 0:
        ans.append([res,val])
print(min(ans))