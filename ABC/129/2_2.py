N = int(input())
W = tuple(map(int, input().split()))
before = 0
after = sum(W)
ans = float('inf')
for i in range(N):
    before += W[i]
    after -= W[i]
    ans = min(ans, abs(before - after))
print(ans)