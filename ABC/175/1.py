S = input()
ans = 0
flag = True
for s in S:
    if flag and s == 'R':
        ans += 1
    if s == 'R':
        ans = max(1, ans)
        flag = True
    else:
        flag = False
print(ans)