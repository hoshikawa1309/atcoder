N, K = map(int, input().split())
prices = list(map(int, input().split()))
prices.sort()
print(sum(prices[:K]))