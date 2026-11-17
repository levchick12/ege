ans = []
for x in range(1,3000):
    cnt = 0
    r = 9**150 + 9**30 - x
    while r:
        if r % 9 == 0: cnt += 1
        r //= 9
    if cnt == 122:
        ans.append(x)
print(min(ans))
