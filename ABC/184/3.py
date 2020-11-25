r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
if r1 == r2 and c1 == c2:
    print(0)
    exit()
if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 + c2) <= 3:
    print(1)
    exit()
flag = False
if abs(r2 - r1) % 2 == 0 and abs(c2 - c1) % 2 == 0:
    flag = True
for i in range(-3, 4):
    for j in range(-3, 4):
        nr = r2 + i
        nc = c2 + j
        if abs(nr - r2) + abs(nc - c2) <= 3 and (r1 + c1 == nr + nc or r1 - c1 == nr - nc):
            flag = True
if flag:
    print(2)
else:
    print(3)