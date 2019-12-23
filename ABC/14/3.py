N = int(input())
lst = [0] * 1000002
color = list(list(map(int,input().split())) for _ in range(N))
for a , b in color:
    lst[a] += 1
    lst[b + 1] -= 1
ans = 0
tmp_ans = 0
for i in range(1000002):
    tmp_ans += lst[i]
    if tmp_ans > ans:
        ans = tmp_ans
print(ans)