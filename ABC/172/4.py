N = int(input())
ans = 0
l = [0] * (10 ** 7 + 1)
for i in range(1, N + 1):
    for j in range(i, N + 1, i):
        l[j] += 1

for i in range(1, N + 1):
    ans += i * l[i]
print(ans)
