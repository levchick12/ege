from string import printable as alph
ans = []
for x in range(10,14):
    for y in range(9,x):
        r1 = int(f'7{alph[x]}37{alph[y]}',14)
        r2 = int(f'9{alph[y]}63', x)
        r3 = int(f'15148', y)
        r = r1 + r2 - r3
        ans.append([r, r // (x+y)])
print(max(ans))
r5 = 14378 + 316323
print(r5)