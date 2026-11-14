r = 5 * 216**3031 + 4 * 36**3042 - 3 * 6**3053 - 3064
count = 0
while r:
    count += r % 6
    r //= 6
print(count)


