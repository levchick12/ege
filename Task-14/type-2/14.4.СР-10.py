from string import printable as alph

for x in alph[:25]:
    r1 = int(f'A4{x}7F2',25)
    r2 = int(f'N{x}G5{x}H', 25)
    r3 = int(f'74{x}M26', 25)
    r = r1 + r2 + r3
    if r % 24 == 0:
        print(r//24)