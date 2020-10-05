N = int(input())
ans = 0
div_list = [0] * (N + 1)
for i in range(1, N + 1):
    for j in range(i, N + 1, i):
        div_list[j] += 1
# print(div_list)

for C in range(1, N):
    ans += div_list[N - C]
print(ans)