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
ans = C[0]
for loop in loops:
    work_loop_sum = []
    now = 0
    tmp_ans = 0
    one_loop_point = sum(loop)
    if one_loop_point <= 0 or K <= len(loop):
        for i in range(1, min(K + 1, len(loop) + 1)):
            tmp_ans = sum(loop[:i])
            for j in range(len(loop)):
                ans = max(tmp_ans, ans)
                tmp_ans = tmp_ans - loop[j] + loop[(i + j) % len(loop)]
    else:
        for i in range(min(K + 1, len(loop) + 1)):
            tmp_ans = sum(loop[:i]) + ((K - i) // len(loop)) * one_loop_point
            for j in range(len(loop)):
                ans = max(tmp_ans, ans)
                tmp_ans = tmp_ans - loop[j] + loop[(i + j) % len(loop)]

print(ans)