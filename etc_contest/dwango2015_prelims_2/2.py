S = input()
ans = 0
flag = False
now = 0
cnt = 0
while now < len(S) - 1:
    if flag and S[now:now + 2] == '25':
        cnt += 1
        now += 2
    elif S[now:now + 2] == '25':
        cnt = 1
        now += 2
        flag = True
    else:
        ans += cnt * (cnt + 1) // 2
        cnt = 0
        now += 1
if cnt:
    ans += cnt * (cnt + 1) // 2
print(ans)