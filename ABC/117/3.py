import heapq
N , M = map(int,input().split())
X = list(map(int,input().split()))
X.sort(reverse=True)
diff = []
heapq.heapify(diff)
for i in range(len(X) - 1):
    heapq.heappush(diff , -1 * (X[i] - X[i + 1]))
for _ in range(N - 1):
    if not diff:
        print("0")
        exit()
    else:
        heapq.heappop(diff)

print(-1 * sum(diff))