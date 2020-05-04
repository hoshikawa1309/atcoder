S = input()
N = len(S)
ans = 0
for i in range(len(S)):
    s = S[i]
    now_floor = i + 1
    upper_floor = N - now_floor
    lower_floor = N - upper_floor - 1
    if s == 'U':
        ans += upper_floor + lower_floor * 2
    elif s == 'D':
        ans += upper_floor * 2 + lower_floor
print(ans)