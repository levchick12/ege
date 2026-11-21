r = 16**820 - 2**761 + 14
cnt = 0
while r:
    if r % 4 == 0: cnt += 1
    r //= 4
print(cnt)