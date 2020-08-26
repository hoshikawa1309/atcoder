N = int(input())
s = []
for _ in range(N):
    s.append(list(input()))

for i in range(N):
    for j in range(N - 1, -1, -1):
        print(s[j][i], end='')
    print()
