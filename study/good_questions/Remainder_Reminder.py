import math
'''
N , K = map(int ,input().split())
ans = 0
for i in range(1,N + 1):
    if i % 1000 == 0:
        print(i)
    for j in range(1,N + 1):
        if i % j >= K:
            ans += 1
print(ans)
'''
N , K = map(int , input().split())
ans = 0
if K == 0:
    print(N * N)
    exit(0)
for b in range(1, N + 1):
    ans += int(N / b) * max(0,b - K) + max(N % b - K + 1 ,0)
print(ans)
