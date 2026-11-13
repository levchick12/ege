from string import printable as alph

for x in alph[:23]:
    r1 = int(f'7{x}38596',23)
    r2 = int(f'14{x}36',23)
    r3 = int(f'61{x}7',23)
    r = r1 + r2 + r3
    if r % 22 == 0:
        print(r // 22)