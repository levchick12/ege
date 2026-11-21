from string import printable as alph

for x in alph[1:13]:
    r1 = int(f'9{x}AB',13)
    r2 = int(f'{x}46C', 16)
    r3 = int(f'B7{x}', 15)
    r = r1 + r2 - r3
    if r % 14 == 0:
        print(r//14)
