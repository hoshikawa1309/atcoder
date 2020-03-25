N = int(input())
A = list(map(int, input().split()))
now = A[0]
ans = 0
for i in range(1, N):
    if now == A[i]:
        ans += 1
        for j in range(1, N + 1):
            if i == N - 1:
                if j != A[i - 1]:
                    A[i] = j
                    break
            else:
                if j != A[i - 1] and j != A[i + 1]:
                    A[i] = j
                    break
    now = A[i]
print(ans)