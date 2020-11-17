N = int(input())
height = [int(input()) for _ in range(N)]
height.append(10 ** 9)
s, t = -1, -1
ans = 0
dp1 = [1] * N
dp2 = [1] * N
for i in range(N - 1):
    if height[i] < height[i + 1]:
        dp1[i + 1] = dp1[i] + 1

for i in range(N - 1, 0, -1):
    if height[i - 1] > height[i]:
        dp2[i - 1] = dp2[i] + 1

for val1, val2 in zip(dp1, dp2):
    ans = max(ans, val1 + val2 - 1)
print(ans)