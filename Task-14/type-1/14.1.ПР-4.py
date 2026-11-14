r = 11 * 15**65 + 18 * 15**38 - 14 * 15**17 + 19 * 15**11 + 18338
count = 0
while r:
    count = r % 15
    r //= 15
print(count)