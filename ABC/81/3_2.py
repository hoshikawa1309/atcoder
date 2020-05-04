from collections import Counter
N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
tate = 0
yoko = 0
i = 0
while i < (N - 1):
    if A[i] == A[i + 1]:
        if tate == 0:
            tate = A[i]
        else:
            yoko = A[i]
        if tate > 0 and yoko > 0:
            break
        i += 1
    i += 1
print(tate * yoko)

