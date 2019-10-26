n , m = map(int,input().split())
war = []
for _ in range(m):
    a , b = map(int,input().split())
    war.append([a,b])
war.sort()
ans = 1
min_right = war[0][1]
max_left = war[0][0]
for i in range(0,m - 1):
    now_left, now_right = war[i][0], war[i][1]
    next_left , next_right = war[i + 1][0] , war[i + 1][1]
    min_right = min(min_right , next_right)
    max_left = max(max_left,next_left)
    if max_left >= min_right:
        ans += 1
        min_right = next_right
print(ans)