ans = []
for x in range(1,3001):
    r = 4**210 + 4**110 - x
    cnt = 0
    while r:
        if r % 4 == 0: cnt += 1
        r //= 4
    ans.append([cnt, x])
print(max(ans, key=lambda x: (x[0], -x[1])))