S = input()
now = S[0]
ans = ""
cnt = 1
for i in range(1, len(S)):
    if now != S[i]:
        ans += now + str(cnt)
        now = S[i]
        cnt = 1
    else:
        cnt += 1
ans += now + str(cnt)
print(ans)