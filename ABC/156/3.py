N = int(input())
X = list(map(int, input().split()))
X_max = max(X)
ans = float('inf')
for i in range(X_max + 1):
    tmp_ans = 0
    for x in X:
        tmp_ans += (x - i) ** 2
    if tmp_ans < ans:
        ans = tmp_ans
print(ans)
