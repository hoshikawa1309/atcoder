N , K = map(int,input().split())
h = list(int(input()) for _ in range(N))
h.sort()
min = 10 ** 10
for i in range(len(h) - K + 1):
    tmp_min = h[i + K - 1] - h[i]
    if min > tmp_min:
        min = tmp_min
print(min)
