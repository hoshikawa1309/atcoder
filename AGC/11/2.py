N = int(input())
# N = 100000
A = list(map(int, input().split()))
# A = [1000000000] * N
A.sort()
sum_val = [0] * N
sum_val[0] = A[0]
for i in range(1, N):
    sum_val[i] = sum_val[i - 1] + A[i]

ans = 1
for i in range(N - 2, -1, -1):
    if 2 * sum_val[i] >= A[i + 1]:
        ans += 1
    else:
        break
print(ans)