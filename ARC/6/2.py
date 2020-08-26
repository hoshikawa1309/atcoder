N, L = map(int, input().split())
lot = []
for _ in range(L):
    lot.append(list(input()))
hit = input()
now = hit.index('o')
# print(hit.index('o'))
right_edge = N + (N - 2)
for i in range(L - 1, -1, -1):
    if now == 0:
        if N > 1 and lot[i][now + 1] == '-':
            now += 2
    elif now == right_edge:
        if lot[i][now - 1] == '-':
            now -= 2
    else:
        if lot[i][now + 1] == '-':
            now += 2
        elif lot[i][now - 1] == '-':
            now -= 2
print(now // 2 + 1)