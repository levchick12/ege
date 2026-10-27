ans= []
for n in range(1,10000):
    r = f'{n:b}'
    if r[-1] == '0':
        r = '10' + r
    else:
        r = '1' + r + '01'
    r = int(r, 2)
    if r > 441:
        ans.append(n)
        ans += [n]
print(min(ans))

