N = int(input())
W = list(map(int ,input().split()))
ans = float('inf')
for i in range(1,N):
    if ans <= abs(sum(W[:i]) - sum(W[i:])):
        break
    ans = abs(sum(W[:i]) - sum(W[i:]))
print(ans)