ans = []
for x in range(1,2031):
    r = 7**170 + 7**100 - x
    cnt = 0
    while r:
        if r % 7 == 0: cnt += 1
        r //= 7
    ans.append(cnt)
print(max(ans))
