N = int(input())
A1 = list(map(int,input().split()))
A2 = list(map(int,input().split()))
ans = A2[-1]
for i in range(N):
    ans += A1[i]
    A2_sum = sum(A2[i : N - 1])
    A1_sum = sum(A1[i + 1 : N])
    if A2_sum > A1_sum and A1[i + 1] <= A2[i]:
        ans += A2_sum
        break
print(ans)