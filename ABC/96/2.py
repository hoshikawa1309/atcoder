A = list(map(int,input().split()))
K = int(input())
A.sort(reverse=True)
for _ in range(K):
    A[0] *= 2
print(sum(A))
