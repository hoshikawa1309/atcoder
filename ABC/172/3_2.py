N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
nowK = K
for A_idx in range(N):
    if nowK < A[A_idx]:
        break
    ans += 1
    nowK -= A[A_idx]
for B_idx in range(M):
    if nowK < B[B_idx]:
        break
    ans += 1
    nowK -= B[B_idx]
tmp_ans = ans
finish = False
for i in range(A_idx - 1, -1, -1):
    nowK += A[i]
    tmp_ans -= 1
    for j in range(B_idx, M):
        if finish or nowK < B[j]:
            break
        nowK -= B[j]
        tmp_ans += 1
        if j == M - 1:
            finish = True
    B_idx = j
    ans = max(tmp_ans, ans)
print(ans)


