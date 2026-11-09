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
    if n % 3 == 0:
        r = r + r[-2:]
    else:
        r = r + str((sum(int(i) for i in r) % 3 * 2) % 3)
    r = int(r,3)
    if r > 520:
        ans.append(r)
print(min(ans))
