N , M = map(int ,input().split())
left = 1
right = N
for i in range(M):
    tmp_left , tmp_right = map(int ,input().split())
    if left < tmp_left:
        left = tmp_left
    if right > tmp_right:
        right = tmp_right
ans = right - left + 1
if ans < 0:
    print("0")
else:
    print(right - left + 1)