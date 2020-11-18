N = int(input())
A = list(int(input()) for _ in range(N))
tmp = list(set(A))
tmp.sort()
d = dict()
for i, a in enumerate(tmp):
    d[a] = i
for a in A:
    print(d[a])