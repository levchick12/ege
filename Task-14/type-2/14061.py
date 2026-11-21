from string import printable as alph
for x in alph[:22]:
    r1 = int(f'27{x}98966',22)
    r2 = int(f'26{x}33', 22)
    r3 = int(f'522{x}5', 22)
    r = r1 + r2 + r3
    if r % 21 == 0:
        print(r//21)