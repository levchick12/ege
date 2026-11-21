for p in range(16, 36):
    r1 = int(f'17496',p)
    r2 = int(f'91f83',p)
    r3 = int(f'd9543',p)
    r = r1 + r2 + r3
    if r % 12 == 0:
        print(p, r // 12)
