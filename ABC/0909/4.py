N , K = map(int,input().split())
ans = 0
S = input()
for i in range(N - 1):
    if S[i] == S[i + 1]:
        ans += 1

print(min(N-1,ans + 2 * K ))
