N = int(input())
A = list(map(int , input().split()))
B = list(map(int , input().split()))
C = list(map(int , input().split()))
ans = 0
for i in range(len(A)):
    ans += B[A[i] - 1]
    if i == len(A) - 1:
        break
    else:
        if A[i + 1] == A[i] + 1:
            ans += C[A[i] - 1]
print(ans)
