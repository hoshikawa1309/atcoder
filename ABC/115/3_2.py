N, K = map(int, input().split())
trees = list(int(input()) for _ in range(N))
trees.sort()
ans = float("inf")
for i in range(N - K + 1):
    tmp_ans = trees[i + K - 1] - trees[i]
    if tmp_ans < ans:
        ans = tmp_ans
print(ans)