N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(N):
    target = A[i]
    if A[target - 1] - 1 == i:
        ans += 1
print(ans // 2)