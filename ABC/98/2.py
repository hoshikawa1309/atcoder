N = int(input())
S = list(input())
ans = 0
for i in range(1 , N - 1):
    before = set(S[:i])
    after = set(S[i:])
    if len(before & after) > ans:
        ans = len(before & after)
print(ans)
