N , K = map(int,input().split())
A = list(map(int,input().split()))
ans = sum(A[0:K])
sum_val = ans
for i in range(N - K):
    sum_val = sum_val - A[i] + A[i + K]
    ans += sum_val
print(ans)