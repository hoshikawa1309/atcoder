N = int(input())
A = list(map(int, input().split()))
ans = [1, A[0]]
for i, a in enumerate(A):
    if i == 0:
        continue
