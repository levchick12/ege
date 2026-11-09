ans = []
for n in range(1, 10000):
    r = f'{n:b}'
    if r[-1] == 0:
        r = r.replace(r[0],'1').replace(r[-1],'0') + '0'
    else:
        r = r.replace(r[0], '1').replace(r[-1],'1') + '1'
    r = int(r, 2)
    if r >= 16:
        ans.append(n)
print(min(ans))

