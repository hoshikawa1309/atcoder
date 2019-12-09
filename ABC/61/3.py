N , K = map(int,input().split())
lst = []
for _ in range(N):
    a , b = map(int,input().split())
    lst.append([a , b])
lst.sort()
for i in range(N):
    if K <= lst[i][1]:
        print(lst[i][0])
        exit()
    else:
        K -= lst[i][1]
