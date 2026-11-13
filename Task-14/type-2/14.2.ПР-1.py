from string import printable as alph

for x in alph[:20]:
    r1 = int(f'627{x}J8',20)
    r2 = int(f'H45I{x}5HIJ',20)
    r3 = int(f'4IDB49J{x}7',20)
    r = r1 + r2 + r3
    if r % 19 == 0:
        print(r // 19)