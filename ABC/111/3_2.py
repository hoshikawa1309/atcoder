from collections import Counter
n = int(input())
lst = list(map(int, input().split()))
counter = Counter(lst)

if len(counter.values()) == 1:
    print(n // 2)
    exit()

num_cnt = list(counter.items())
num_cnt.sort(key=lambda x: x[1], reverse=True)
max_num = num_cnt[0][0]
second_max_num = num_cnt[1][0]
tmp_ans = 0
for i in range(n):
    if i % 2 == 0 and max_num == lst[i] or \
            i % 2 == 1 and second_max_num == lst[i]:
        continue
    tmp_ans += 1
ans = 0
for i in range(n):
    if i % 2 == 1 and max_num == lst[i] or \
            i % 2 == 0 and second_max_num == lst[i]:
        continue
    ans += 1
print(min(ans, tmp_ans))