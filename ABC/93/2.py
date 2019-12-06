A, B, K = map(int,input().split())
ansList = []
for i in range(K):
    if A + i > B:
        break
    ansList.append(A + i)
for i in range(K - 1,-1,-1):
    if B - i < A or B - i in ansList:
        continue
    ansList.append(B - i)
for c in ansList:
    print(c)