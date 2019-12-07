N = int(input())
K = int(input())
x = list(map(int,input().split()))
ans = 0
for i in range(N):
    distance = min(x[i] , K - x[i])
    ans += distance * 2
print(ans)