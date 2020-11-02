N = int(input())
height = [int(input()) for _ in range(N)]
height.append(10 ** 9)
s, t, u = -1, -1, -1
ans = 0
i = 0
while i < N:
    now_h = height[i]
    next_h = height[i + 1]
    if now_h < next_h:
        if s == -1:
            s = i
        else:
            t = i
    elif now_h == next_h:
        s, t, u = -1, -1, -1
    else:
        if s != -1:
            u = i + 1
            while i < N and height[i] > height[i + 1]:
                ans = max(ans, u - s + 1)
                i += 1
            if height[i] < height[i + 1]:
                s = i
            else:
                s = -1
            t, u = -1, -1
        else:
            s, t, u = -1, -1, -1
    i += 1
print(ans)