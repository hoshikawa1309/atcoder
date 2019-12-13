N = int(input())
A = list(int(input()) for _ in range(N))
B = []
for idx , val in enumerate(A):
    B.append([val , idx])
B.sort()
B[0].append(0)
now = 0
for i in range(1 , N):
    if B[i][0] != B[i - 1][0]:
        now += 1
    B[i].append(now)
B.sort(key = lambda x: x[1])
for b in B:
    print(b[2])