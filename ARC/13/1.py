import itertools
N, M, L = map(int, input().split())
P, Q, R = map(int, input().split())
ans = 0
for i, j, k in itertools.permutations((P, Q, R)):
    ans = max(ans, (N // i) * (M // j) * (L // k))
print(ans)