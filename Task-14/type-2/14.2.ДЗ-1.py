from string import printable as alph

for x in alph[:27]:
    r1 = int(f'8{x}38{x}68',27)
    r2 = int(f'37{x}3163',27)
    r = r1 + r2
    if r % 26 == 0:
        print(r// 26)
