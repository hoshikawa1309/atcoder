N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))
loop_flags = [False] * N
loops = []
for i in range(N):
    if loop_flags[i]:
        continue
    next_cell = i
    loop = []
    while not loop_flags[next_cell]:
        loop_flags[next_cell] = True
        loop.append(C[next_cell])
        next_cell = P[next_cell] - 1
    if loop:
        loops.append(loop)
# print(loops)

ans = -float('inf')
for loop in loops:
    sum_score = sum(loop)
    if sum_score > 0:
        sum_val = sum_score * (K // len(loop))
        remain_K = K % len(loop)
    else:
        sum_val = 0
        remain_K = min(len(loop), K)
    for i in range(1, remain_K + 1):
        target = sum_val
        target += sum(loop[:i])
        ans = max(target, ans)
        for j in range(len(loop)):
            target = target - loop[j] + loop[(i + j) % len(loop)]
            ans = max(target, ans)
print(ans)