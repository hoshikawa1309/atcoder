N , M = map(int,input().split())
A = []
B = []
C = []
for _ in range(M):
    a , b = map(int , input().split())
    C.append(list(map(int , input().split())))
    A.append(a)
    B.append(b)
dp = [[-1] * M for _ in range(N)]
