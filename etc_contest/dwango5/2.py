N, K = map(int, input().split())
a = list(map(int, input().split()))
start = 0
candidates = []
for i in range(start, N - 1):
    now = [a[start]]
    for j in range(i + 1, N):
        candidates.append(now)
        now.append(a[j])
print(candidates)
