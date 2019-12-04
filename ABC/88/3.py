c = list(list(map(int,input().split())) for _ in range(3))

for b1 in range(101):
    a = []
    b = []
    a1 = c[0][0] - b1
    if a1 < 0:
        break
    a.append(a1)
    b.append(b1)
    for b2 in range(101):
        a2 = c[1][1] - b2
        if a2 < 0:
            break
        a.append(a2)
        b.append(b2)
        for b3 in range(101):
            a3 = c[2][2] - b3
            if a3 < 0:
                break
            a.append(a3)
            b.append(b3)
            for i in range(3):
                for j in range(3):
                    if a[j] + b[i] != c[i][j]:
                        break
                    if i == 2 and j == 2:
                        print("Yes")
                        exit()
                if a[j] + b[i] != c[i][j]:
                    break
            b.pop()
            a.pop()
        a.pop()
        b.pop()
print("No")