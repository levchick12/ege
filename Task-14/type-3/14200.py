ans = []
for x in range(1, 2031):
    r = 2**2025 + 2**2024 - 2**2021 - x
    cnt = 0
    while r:
        if r % 4 == 0: cnt += 1
        r //= 4
    ans.append([cnt, x])
print(max(ans))