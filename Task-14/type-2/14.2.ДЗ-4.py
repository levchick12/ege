from string import printable as alph

cnt = 0
for x in range(10, 36):
    for y in range(36):
        cnt += 1
        r1 = int(f'73{x}1{y}', 36)
        r2 = int(f'49{y}6', x)
        r = r1 + r2
        print(r, cnt)