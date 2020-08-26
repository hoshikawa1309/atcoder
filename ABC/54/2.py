N, M = map(int, input().split())
A = []
for _ in range(N):
    Ai = tuple(input())
    A.append(Ai)
A = tuple(A)
B = []
for _ in range(M):
    Bi = tuple(input())
    B.append(Bi)
B = tuple(B)


for i in range(N - M + 1):
    for j in range(N - M + 1):
        contain = True
        for k in range(M):
            if not contain:
                break
            for l in range(M):
                if A[i + k][j + l] != B[k][l]:
                    contain = False
                    break
        if contain:
            print('Yes')
            exit()
print('No')
