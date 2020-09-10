from collections import Counter
H, W = map(int, input().split())
a = ''
for _ in range(H):
    a += input()
cnt_counter = list(Counter(a).values())
yes_flag = False
if H % 2 == 0 and W % 2 == 0:
    if all([i % 4 == 0 for i in cnt_counter]):
        yes_flag = True
elif H % 2 == 1 and W % 2 == 1:
    two_cnt = (H // 2) + (W // 2)
    four_cnt = (H // 2) * (W // 2)
    for i in range(len(cnt_counter)):
        if cnt_counter[i] % 2 == 1:
            cnt_counter[i] -= 1
            break
    else:
        print('No')
        exit()
    for i in range(len(cnt_counter)):
        if cnt_counter[i] <= 0:
            continue
        if cnt_counter[i] % 2 == 0 and cnt_counter[i] % 4 != 0:
            two_cnt -= 1
            cnt_counter[i] -= 2
        if two_cnt == 0:
            break
    for i in range(len(cnt_counter)):
        if cnt_counter[i] <= 0:
            continue
        if cnt_counter[i] % 4 != 0:
            break
        while two_cnt > 1 and cnt_counter[i]:
            two_cnt -= 2
            cnt_counter[i] -= 4
        while four_cnt > 0 and cnt_counter[i]:
            four_cnt -= 1
            cnt_counter[i] -= 4
    if two_cnt == four_cnt == 0:
        yes_flag = True
else:
    if H % 2 == 0:
        two_cnt = H // 2
    else:
        two_cnt = W // 2
    four_cnt = (H // 2) * (W // 2)
    for i in range(len(cnt_counter)):
        if cnt_counter[i] % 2 == 0 and cnt_counter[i] % 4 != 0:
            two_cnt -= 1
            cnt_counter[i] -= 2
        if two_cnt == 0:
            break
    for i in range(len(cnt_counter)):
        if cnt_counter[i] <= 0:
            continue
        if cnt_counter[i] % 4 != 0:
            break
        while two_cnt > 1 and cnt_counter[i]:
            two_cnt -= 2
            cnt_counter[i] -= 4
        while four_cnt > 0 and cnt_counter[i]:
            four_cnt -= 1
            cnt_counter[i] -= 4
    if two_cnt == four_cnt == 0:
        yes_flag = True
if yes_flag:
    print('Yes')
else:
    print('No')