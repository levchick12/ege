# r = f'{2048:b}'
# r1 = int('111111111111',2)
# print(r, r1)

from string import printable as alph

def convert(num, sys):
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1] if res else '0'

ans = []
for n in range(1,10000):
    r = convert(n,3)
    if n % 2 == 0:
        r = r + r[-2:]
    else:
        r = r + convert(sum(map(int, r)), 3)
    r = int(r,3)
    if n > 9:
        ans.append([r,n])
print(min(ans))
print(ans)

# r =1920*1080*8*32*64
# print(r)
