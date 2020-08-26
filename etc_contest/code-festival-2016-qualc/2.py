import heapq
K, T = map(int, input().split())
a = tuple(map(int, input().split()))
cakes = []
heapq.heapify(cakes)
for i in range(T):
    heapq.heappush(cakes, [-1*a[i], i])
# print(cakes)
now = -1
ans = 0
for _ in range(K):
    cake_num, cake_idx = heapq.heappop(cakes)
    cake_num *= -1
    if cake_idx == now and len(cakes) > 1 and cakes[0][0] != 0:
        next_cake_num, next_cake_idx = heapq.heappop(cakes)
        next_cake_num *= -1
        next_cake_num -= 1
        heapq.heappush(cakes, [-1 * next_cake_num, next_cake_idx])
        now = next_cake_idx
    else:
        cake_num -= 1
        if now == cake_idx:
            ans += 1
        now = cake_idx
    heapq.heappush(cakes, [-1 * cake_num, cake_idx])
# print(cakes)
print(ans)

