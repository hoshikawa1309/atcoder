N = int(input())
open = []
for _ in range(N):
    open.append(list(map(int,input().split())))
sales = []
for _ in range(N):
    sales.append(list(map(int,input().split())))

ans = -float("inf")
for i in range(1 , 1024):
    sum_val = 0
    mapping = []
    for k in range(N):
        cnt = 0
        for j in range(10):
            if i >> j & 1 and open[k][j] == 1:
                cnt += 1
        mapping.append(cnt)
    for k in range(N):
        sum_val += sales[k][mapping[k]]
    if sum_val > ans:
        ans = sum_val
print(ans)
