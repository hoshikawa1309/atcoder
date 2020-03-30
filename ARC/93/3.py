N = int(input())
A = list(map(int, input().split()))
A.append(0)
sum_val = 0
now = 0
for i in range(N + 1):
    sum_val += abs(A[i] - now)
    now = A[i]

for i in range(1 , N + 1):
    if A[i - 1] >= 0:
        if A[i - 1] > A[i]:
            print(sum_val - min(abs(A[i - 1] - A[i - 2]), abs(A[i - 1])) * 2)
        else:
            print(sum_val)
    elif A[i - 1] < 0:
        if A[i - 1] < A[i]:
            print(sum_val - abs(A[i - 1] - A[i]) * 2)
        else:
            print(sum_val)
