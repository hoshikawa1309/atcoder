c = list(list(map(int,input().split())) for _ in range(3))
a = []
b = []
for i in range(3):
    a.append(min(c[i]))
    b.append(min(c[0][i] , c[1][i],c[2][i]))
if b == c[0] and c[0] == c[1] == c[2]:
    a = [0,0,0]
if a == [c[0][0] , c[1][0] ,c[2][0]] and c[0][0] == c[0][1] == c[0][2] and c[1][0] == c[1][1] == c[1][2] and c[2][0] == c[2][1] == c[2][2]:
    b = [0, 0, 0]

for i in range(3):
    for j in range(3):
        if c[i][j] != a[i] + b[j]:
            print("No")
            exit()
print("Yes")