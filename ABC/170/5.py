import heapq

N, Q = map(int, input().split())
AtCoder = [] * (2 * 10 ** 5)
print(len(AtCoder))
for _ in range(N):
    rate, begin = map(int, input().split())
    AtCoder[begin - 1].append(-rate)
print(AtCoder)
