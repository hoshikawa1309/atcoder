N = int(input())
A = list(map(int, input().split()))
A.append(0)
A.insert(0, 0)
sum_val = 0
now = 0
for i in range(N + 1):
    sum_val += abs(A[i] - A[i + 1])

for i in range(1 , N + 1):
    print(sum_val - (abs(A[i-1] - A[i]) + abs(A[i] - A[i + 1])) + abs(A[i - 1] - A[i + 1]))
