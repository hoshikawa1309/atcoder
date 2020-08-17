N, K = map(int, input().split())
k3 = 1
k2 = 3 * (N - 1)
k1 = 6 * (K - 1) * (N - K)
print((k1 + k2 + k3) / (N ** 3))