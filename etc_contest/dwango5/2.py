N, K = map(int, input().split())
A = list(map(int, input().split()))
candidates = []
for i, _ in enumerate(A):
    add_num = 0
    for a in A[i:]:
        add_num += a
        candidates.append(add_num)

ans = 0
for i in range(40, -1, -1):
    k_candidates = []
    for candidate in candidates:
        if candidate & (1 << i):
            k_candidates.append(candidate)
    if len(k_candidates) >= K:
        ans += 1 << i
        candidates = k_candidates
print(ans)