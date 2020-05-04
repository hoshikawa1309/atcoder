N, L = map(int, input().split())
apples = [i + L for i in range(N)]
apple_pie = sum(apples)
ans = float('inf')
for apple in apples:
    if ans > abs(apple):
        ans = abs(apple)
        val = apple
print(sum(apples) - val)