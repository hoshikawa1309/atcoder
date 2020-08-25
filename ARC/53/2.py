from collections import Counter
S_counter = Counter(input())
odd_cnt = 0
cnt = 0
for val in S_counter.values():
    if val % 2 == 1:
        odd_cnt += 1
    cnt += val // 2
# print(cnt)
# print(odd_cnt)
if odd_cnt <= 1:
    print(cnt * 2 + odd_cnt)
else:
    print((cnt // odd_cnt) * 2 + 1)