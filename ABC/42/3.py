N  ,K = map(int,input().split())
D = list(input())
now = N
s = set(list(str(now)))
d = set(D)
while s & d != set():
    now += 1
    #print(now)
    s = set(list(str(now)))
print(now)




