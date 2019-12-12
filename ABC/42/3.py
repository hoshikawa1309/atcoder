N  ,K = map(int,input().split())
D = list(input())
use = []
for i in range(10):
    if not i in D:
        use.append(i)
now = N
s = set(list(str(now)))
d = set(D)
while s & d != set():
    now += 1
    #print(now)
    s = set(list(str(now)))
print(now)




