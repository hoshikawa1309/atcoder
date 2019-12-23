N = int(input())
a = list(map(int,input().split()))
now = 1
for i in range(N):
    if now == a[i]:
        now += 1
if now == 1:
    print("-1")
else:
    print(N - now + 1)