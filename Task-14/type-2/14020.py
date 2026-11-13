from string import printable as alph

for x in alph[:22]:
    r1 = int(f'18{x}89957',22)
    r2 = int(f'80{x}33',22)
    r3 = int(f'521{x}6',22)
    r = r1 + r2 + r3
    if r % 21 == 0:
        print(r // 21)
