S = input()
ans = [0] * (len(S) + 1)

for i in range(len(S)):
    if S[i] == '<':
        ans[i + 1] = ans[i] + 1

for i in range(len(S) - 1, -1, -1):
    if S[i] == '>':
        ans[i] = max(ans[i + 1] + 1, ans[i])
print(sum(ans))
