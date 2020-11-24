H, W, D = map(int, input().split())
stage = [list(map(int, input().split())) for _ in range(H)]
coordinate_dict = {}
for row in range(H):
    for column in range(W):
        coordinate_dict[stage[row][column] - 1] = (row, column)

dp = [0] * (H * W)
for i in range(D):
    for j in range(i + D, H * W, D):
        from_num = coordinate_dict[j - D]
        to_num = coordinate_dict[j]
        dist = abs(from_num[0] - to_num[0]) + abs(from_num[1] - to_num[1])
        dp[j] += dp[j - D] + dist

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    print(dp[r - 1] - dp[l - 1])