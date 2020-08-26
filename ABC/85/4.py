import math
N, H = map(int, input().split())
a_l = []
b_l = []
for _ in range(N):
    a, b = map(int, input().split())
    a_l.append(a)
    b_l.append(b)

a_l.sort(reverse=True)
b_l.sort(reverse=True)
ans = 0
for i in range(N):
    if a_l[0] >= b_l[i]:
        break
    else:
        ans += 1
        H = max(H - b_l[i], 0)
        if H <= 0:
            break
ans += math.ceil(H / a_l[0])
print(ans)