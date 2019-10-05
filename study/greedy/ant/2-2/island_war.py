N , M = map(int ,input().split())

bridge = [list(map(int , input().split())) for _ in range(M)]

bridge.sort()
ans = 1
left , right = bridge[0][0] , bridge[0][1]

for tmp_left , tmp_right in bridge[1:]:
    if tmp_left < right:
        right = min(right , tmp_right)
        left = max(left , tmp_left)
    else:
        ans += 1
        left = tmp_left
        right = tmp_right
print(ans)
