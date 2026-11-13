from string import printable as alph

def convert(num, sys):
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1] if res else '0'
ans = []
for n in range(1,10000):
    r = convert(n, 3)
    if (r.count('1') + r.count('2') * 2) % 3 == 0:
        r = r + '212'
    else:
        r = r + convert((r.count('1') + r.count('2') * 2)*2,3)
    r = int(r,3)
    print(r)