ans = []
for x in range(1,2031):
    r = 6**2030 + 6**100 - x
    cnt = 0
    while r:
        if r % 6 == 0: cnt += 1
        r //= 6
    ans.append(cnt)
print(max(ans))

