r = 51 * 7**12 - 7**3 - 22
cnt = 0
while r:
    cnt += r % 7
    r //= 7
print(cnt)
