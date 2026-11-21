from string import printable as alph

for x in alph[:16]:
    r1 = int(f'11{x}73',16)
    r2 = int(f'94662{x}53{x}', 16)
    r3 = int(f'6{x}41', 16)
    r4 = int(f'31{x}77', 16)
    r5 = int(f'9{x}82{x}{x}181', 16)
    r = r1 + r2 + r3 + r4 + r5
    if r % 15 == 0:
        print(r//15)