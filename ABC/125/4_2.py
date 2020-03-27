N = int(input())
A = list(map(int, input().split()))
minus_cnt = 0
for i in range(len(A)):
    if A[i] < 0:
        minus_cnt += 1
        A[i] = -A[i]
if minus_cnt % 2 == 0:
    print(sum(A))
else:
    tmp = float("inf")
    for a in A:
        if tmp > abs(a):
            tmp = a
    print(sum(A) - 2 * tmp)
