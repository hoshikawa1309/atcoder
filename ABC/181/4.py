now = 8
eight_list = []
while now < 1000:
    # print(str(now))
    eight_list.append(str(now))
    now += 8
from collections import defaultdict
S = input()
if len(S) < 3:
    if S in eight_list or S[::-1] in eight_list:
        print('Yes')
    else:
        print('No')
    exit()
for idx, eight in enumerate(eight_list):
    if len(eight) == 1:
        eight_list[idx] = '00' + eight
    elif len(eight) == 2:
        eight_list[idx] = '0' + eight
# print(eight_list)
num_cnt = [0] * 10
for c in S:
    num_cnt[int(c)] += 1
# print(num_cnt)
for eight in eight_list:
    d = defaultdict(int)
    for c in eight:
        d[c] += 1
    for key, val in d.items():
        if num_cnt[int(key)] < d[key]:
            break
    else:
        # print(d.items())
        print('Yes')
        exit()
print('No')