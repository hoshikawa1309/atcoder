N = int(input())
now_x = 0
now_y = 0
now_t = 0
Flag = False
for i in range(N):
    t , x, y = map(int,input().split())
    dx = abs(x - now_x)
    dy = abs(y - now_y)
    dt = abs(t - now_t)
    if (dt - (dx + dy)) % 2 != 0 or dt < (dx + dy):
        Flag = True
    now_x = x
    now_y = y
    now_t = t
print("No" if Flag else "Yes")