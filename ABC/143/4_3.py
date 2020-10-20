N = int(input())
L = tuple(map(int, input().split()))
ans = 0
for i in range(N - 2):
    for j in range(i, N - 1):
        if i == j:
            continue
        for k in range(j, N):
            if i == k or j == k:
                continue
            if L[i] < L[j] + L[k] and L[j] < L[i] + L[k] and L[k] < L[j] + L[i]:
                ans += 1
print(ans)