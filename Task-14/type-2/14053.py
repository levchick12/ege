from string import printable as alph

for x in alph[:22]:
    r1 = int(f'12313{x}57',22)
    r2 = int(f'1{x}34561', 22)
    r = r1 + r2
    if r % 21 == 0:
        print(r//21)
