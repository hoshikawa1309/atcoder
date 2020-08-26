N, K, M, R = map(int, input().split())
scores = []
for _ in range(N - 1):
    score = int(input())
    scores.append(score)
scores.sort(reverse=True)
if N == K:
    sum_val = sum(scores[:K - 1])
    if sum_val / K > R:
        print(0)
    elif (sum_val + M) / K < R:
        print(-1)
    else:
        print(R * K - sum_val)
else:
    sum_val = sum(scores[:K])
    if sum_val / K >= R:
        print(0)
    elif (sum_val - scores[K - 1] + M) / K < R:
        print(-1)
    else:
        print(R * K - (sum_val - scores[K - 1]))