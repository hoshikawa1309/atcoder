import bisect
T = int(input())
N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))
if N < M:
    print("no")
    exit()
i = 0
cnt = 0
for b in B:
    while i != N:
        if A[i] <= b <= A[i] + T:
            cnt += 1
            i += 1
            break
        i += 1


if cnt == M:
    print("yes")
else:
    print("no")