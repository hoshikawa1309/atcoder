from collections import Counter
N = int(input())
A = list(map(int,input().split()))
A.sort(reverse=True)
Flag = False
base = 0
height = 0
ans = 0
for i in range(N - 1):
    if Flag:
        Flag = False
        continue
    if A[i] == A[i + 1] and base == 0:
        base = A[i]
        Flag = True
    elif A[i] == A[i + 1]:
        height = A[i]
        Flag = True
    area = base * height
    if area > ans:
        ans = area
print(ans)