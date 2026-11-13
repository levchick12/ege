from string import printable as alph

for x in alph[:19]:
    r1 = int('98x79641'.replace('x',x),19)
    r2 = int('36' + x + '14',19)
    r3 = int(f'73{x}4',19)
    r = r1+r2+r3
    if r % 18 == 0:
        print(r // 18)
