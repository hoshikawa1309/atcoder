N, K = map(int,input().split())
ans = 0
while N >= 1:
    N /= K
    ans += 1
print(ans)