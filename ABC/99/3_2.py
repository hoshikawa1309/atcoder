N = int(input())
sum_list = []
for i in range(8):
    sum_list.append(6 ** (i + 1))
for i in range(5):
    sum_list.append(9 ** (i + 1))
print(sum_list)
ans = float('inf')
for i in range(2 ** 13 + 1):
    now = 0
    cnt = 0
    work = N
    for j in range(13):
        if (i >> j) & 1:
            cnt += work // sum_list[j]
            work -= sum_list[j] * (work // sum_list[j])
    print(ans)
    ans = min(ans, work + cnt)
print(ans)
