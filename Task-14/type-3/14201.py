ans = []
for x in range(1, 2031):
    r = 3**100 - x
    cnt = 0
    while r:
        if r % 3 == 0: cnt += 1
        r //= 3
    ans.append([cnt, x])
print(max(ans))