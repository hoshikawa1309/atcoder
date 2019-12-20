N = int(input())
A = list(map(int,input().split()))
ans = 0
aokimax = 0
# i : 高橋くんがとる値
for i in range(N):
    # j : 青木くんがとる値を全探索
    aokimax = 0
    for j in range(N):
        if i == j:
            continue
        start = min(i , j)
        end = max(i , j) + 1
        work = A[start:end]
        tmp_ans = sum(work[::2])
        aoki = sum(work[1::2])
        if aoki > aokimax:
            aokimax = aoki
            if tmp_ans > ans:
                ans = tmp_ans
print(ans)
