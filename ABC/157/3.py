N, M = map(int, input().split())
sc = []
s_max = 0
for _ in range(M):
    s, c = map(int, input().split())
    sc.append([s, str(c)])
    s_max = max(s, s_max)

if N == 1:
    start = 0
else:
    start = 10 ** (N - 1)
for i in range(start, 1000):
    str_i = str(i)
    len_i = len(str_i)
    for s, c in sc:
        if len_i != N:
            break
        if str_i[s - 1] != c:
            break
    else:
        print(i)
        exit()
print(-1)