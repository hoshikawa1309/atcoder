'''
N , M = map(int,input().split())
A = []
B = []
C = []
for _ in range(M):
    a , b = map(int , input().split())
    C.append(list(map(int , input().split())))
    A.append(a)
    B.append(b)
dp = [[-1] * M for _ in range(N)]
'''

n, m = [int(x) for x in input().split()]

INF = int(10e8 + 1)
dp = [INF] * (1 << n)
dp[0] = 0

for j in range(m):
    cost = int(input().split()[0])

    boxes = [int(x) - 1 for x in input().split()]
    mask = 0

    mask = sum(1 << box for box in boxes)

    for i in range(1 << n):
        if dp[i] + cost < dp[i | mask]:
            dp[i | mask] = dp[i] + cost

res = dp[-1] if dp[-1] != INF else -1
#print(dp)
print(res)