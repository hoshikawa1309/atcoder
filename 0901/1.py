S = input()
T = input()
ans = 0
for i in range(3):
    if S[i] == T[i]:
        ans += 1
print(ans)
