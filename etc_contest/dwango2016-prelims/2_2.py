N = int(input())
K = list(map(int, input().split()))
ans = [-1] * N
ans[0] = K[0]
ans[-1] = K[-1]
for i in range(N - 2):
    ans[i + 1] = min(K[i], K[i + 1])
print(*ans)