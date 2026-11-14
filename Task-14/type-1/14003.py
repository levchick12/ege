r = 3*4**38 + 2*4**23 + 4**20 + 3*4**5 + 2*4**4 + 1
count=0
while r:
    if r % 16 == 0: count += 1
    r //= 16
print(count)