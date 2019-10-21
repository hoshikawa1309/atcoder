n,m=map(int,input().split())
a=[]
for i in range(m):
    x,y=map(int,input().split())
    a.append([x,y])
ans=0
#print(a)
for i in range(m):
    b=[a[i][0]]
    #print(b)
    #print("i : ",i)
    for j in range(n):
        #print("j : ",j)
        for k in range(m):
            print("i : {} , j : {} ,k : {}".format(i,j,k))
            if k!=i and a[k][0] in b:
                b.append(a[k][1])
            elif k!=i and a[k][1] in b:
                b.append(a[k][0])
            print(b)
    #print(b)
    if a[i][1] not in b:
        ans+=1
#print(b)
print(ans)
