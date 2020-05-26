c = list(list(map(int, input().split())) for _ in range(3))
c00 = c[0][0]
c11 = c[1][1]
c22 = c[2][2]
for a0 in range(c00 + 1):
    for a1 in range(c11 + 1):
        for a2 in range(c22 + 1):
            A = [a0, a1, a2]
            B = [c00 - a0, c11 - a1, c22 - a2]
            tmp = []
            for a in A:
                row = []
                for b in B:
                    row.append(a + b)
                tmp.append(row)
            if tmp == c:
                print('Yes')
                exit()
print('No')

