'''
N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
'''
with open('./b09.txt') as f:
    N, M, K = map(int, f.readline().split())
    A = list(map(int, f.readline().split()))
    B = list(map(int, f.readline().split()))

A_cnt = 0
B_cnt = 0
ans = 0
nowK = K
for A_idx in range(N):
    if nowK < A[A_idx]:
        break
    ans += 1
    nowK -= A[A_idx]
    A_cnt += 1
for B_idx in range(M):
    if nowK < B[B_idx]:
        break
    ans += 1
    nowK -= B[B_idx]
    B_cnt += 1
tmp_ans = ans
finish = False
for i in range(A_cnt, 0, -1):
    nowK += A[i - 1]
    tmp_ans -= 1
    for j in range(B_cnt, M):
        if finish or nowK < B[j]:
            break
        nowK -= B[j]
        tmp_ans += 1
        B_cnt += 1
    ans = max(tmp_ans, ans)
print(ans)


