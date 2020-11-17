N = int(input())
A = list(map(int,input().split()))
ans = -float('inf')
for t in range(N):
    aoki_max = -float('inf')
    for a in range(N):
        if t == a:
            continue
        start_idx = min(a, t)
        end_idx = max(a, t)
        takahashi = 0
        aoki = 0
        for i in range(start_idx, end_idx + 1, 2):
            takahashi += A[i]
        for i in range(start_idx + 1, end_idx + 1, 2):
            aoki += A[i]
        if aoki_max < aoki:
            tmp_ans = takahashi
            aoki_max = aoki
    ans = max(tmp_ans, ans)
print(ans)