num = 7 * 729**543 - 6 * 81**765 - 5 * 9**987 - 20
count = 0
while num:
    if num % 9 == 8: count += 1
    num //= 9
print(count)
