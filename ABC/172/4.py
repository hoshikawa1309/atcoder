N = int(input())
divisions = [0] * (10 ** 7 + 1)
for i in range(1, N + 1):
    for j in range(i, N + 1, i):
        divisions[j] += 1
ans = 0
for i in range(1, N + 1):
    now = i * divisions[i]
    ans += i * divisions[i]
print(ans)