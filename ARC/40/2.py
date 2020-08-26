N, R = map(int, input().split())
S = list(input())
ans = 0
will_paint_num = 0
last_will_paint = 0
for i in range(N):
    if S[i] == '.':
        will_paint_num += 1
        last_will_paint = i

now = 0
while will_paint_num:
    ans += 1
    if now + R - 1 >= last_will_paint:
        for i in range(now, min(R + now, N)):
            if S[i] == '.':
                S[i] = 'o'
                will_paint_num -= 1
    elif S[now] == 'o':
        now += 1
    elif S[now] == '.':
        for i in range(now, min(R + now, N)):
            if S[i] == '.':
                S[i] = 'o'
                will_paint_num -= 1

print(ans)

