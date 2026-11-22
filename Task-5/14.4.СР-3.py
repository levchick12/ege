ans = []
for n in range(1,10000):
    r = f'{n:b}'
    if sum(map(int, r)) % 2 == 0:
        r = '11' + r[2:] + '1'
    else:
        if r.count('1') > r.count('0'):
            r = r + '0'
        else:
            r = r + '1'
    r = int(r,2)
    if r > 271:
        ans.append(n)
print(min(ans))

