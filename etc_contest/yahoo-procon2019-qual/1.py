N, K = map(int, input().split())
l = []
for i in range(1, N + 1, 2):
    l.append(i)
if len(l) >= K:
    print('YES')
else:
    print('NO')