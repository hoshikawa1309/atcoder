N, M = map(int,input().split())
sc = []
for _ in range(M):
    s, c = input().split()
    s = int(s)
    if s > N:
        print('-1')
        exit()
    sc.append([s, c])

ans = -1
if N == 1:
    start = 0
else:
    start = 10 ** (N - 1)
for i in range(start, 10 ** N):
    str_num = str(i)
    for s, c in sc:
        if str_num[s - 1] != c:
            break
    else:
        ans = i
        break
print(ans)
