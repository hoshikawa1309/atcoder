import heapq
X, Y, A, B, C = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
p.sort(reverse=True)
q.sort(reverse=True)
r.sort(reverse=True)
candidates = []
for i in range(X):
    candidates.append(-1 * p[i])
for i in range(Y):
    candidates.append(-1 * q[i])
for i in range(C):
    candidates.append(-1 * r[i])
heapq.heapify(candidates)
ans = 0
for _ in range(X + Y):
    val = heapq.heappop(candidates)
    ans += val
print(-ans)
