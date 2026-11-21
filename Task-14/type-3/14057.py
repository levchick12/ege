ans = []
for x in range(1,3001):
    r = 9 * 11**210 + 8 * 11**150 - x
    cnt = 0
    while r:
        if r % 11 == 0: cnt += 1
        r //= 11
    if cnt == 60:
        ans.append(x)
print(max(ans))
