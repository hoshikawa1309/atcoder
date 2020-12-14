N = 200
a=[[1]]
for i in range(1,N):
    tmp=[1]
    if i >1:
        for j in range(1,i):
            tmp.append(a[i-1][j-1]+a[i-1][j])
    tmp.append(1)
    a.append(tmp)


L = int(input())
print(a[L - 1][11])
