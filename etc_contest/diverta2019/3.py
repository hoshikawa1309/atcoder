N = int(input())
ans = 0
a_cnt = 0
b_cnt = 0
a_and_b_cnt = 0
for _ in range(N):
    s = input()
    for i in range(len(s) - 1):
        if s[i:i + 2] == 'AB':
            ans += 1
    if s[0] == 'B' and s[-1] == 'A':
        a_and_b_cnt += 1
    elif s[-1] == 'A':
        a_cnt += 1
    elif s[0] == 'B':
        b_cnt += 1
add = min(a_cnt, b_cnt)
if a_cnt + b_cnt:
    add += a_and_b_cnt
else:
    add += a_and_b_cnt - 1
print(ans + add)