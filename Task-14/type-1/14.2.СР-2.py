r = 729**8  - 3**18 + 85
count = 0
while r:
    if r % 9 == 0: count += 1
    r //= 9
print(count)