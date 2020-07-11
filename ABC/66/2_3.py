S = input()[:-1]
ans = 0
for i in range(1, len(S) // 2 + 1):
    if S[:i] == S[i:i * 2]:
        ans = i * 2
print(ans)