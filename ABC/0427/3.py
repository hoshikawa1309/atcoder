import sys
sys.setrecursionlimit(500000)
def gcd(x , y):
    while y != 0:
        x , y = y , x % y
    return x
N = int(input())
A = list(map(int ,input().split()))
max_val = 0
if N == 2:
    print(max(A[1], A[0]))
    exit()
right = []
left = []
work_right = gcd(A[N - 2] , A[N - 1])
right.append(A[N - 1])
work_left = gcd(A[0] , A[1])
left.append(A[0])
for i in range(1 , N - 1):
    work_left = gcd(work_left , A[i])
    left.append(work_left)
    work_right = gcd(work_right , A[N - i - 1])
    right.append(work_right)
print(right)
print(left)
right.reverse()
max_val = 0
for i in range(N):
    if i == 0:
        max_val = right[0]
    elif i == N - 1:
        if max_val < left[-1]:
            max_val = left[-1]
    else:
        tmp = gcd(right[i] , left[i - 1])
        if tmp > max_val:
            max_val = tmp
print(max_val)
'''
for i in range(N):
    work = A[:i] + A[i + 1:]
    for j in range(1 , len(work)):
        if j == 1:
            tmp = gcd(work[0],work[1])
        else:
            tmp = gcd(tmp , work[j])
    if max_val < tmp:
        max_val = tmp
print(max_val)
'''