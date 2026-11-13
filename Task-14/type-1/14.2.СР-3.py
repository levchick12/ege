r = 283**382 + 9**15 + 2**3
cnt = 0
cnt1 = 0
while r:
    if r % 14 == 11: cnt += 1
    if r % 14 == 12: cnt1 += 1
    r //= 14
print(abs(cnt - cnt1))
