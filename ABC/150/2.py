N = int(input())
S = list(input())
ABC_list = ["A","B","C"]
idx = 0
ans = 0
for i in range(N - 2):
    if ABC_list == S[i:i + 3]:
        ans += 1
print(ans)