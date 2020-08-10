from collections import defaultdict


H, W = map(int, input().split())

matrix = []
for _ in range(H):
    matrix.append(list(input()))

counter = defaultdict(int)
for i in range(H):
    for j in range(W):
        counter[matrix[i][j]] += 1


if H % 2 == 0 and W % 2 == 0:
    for v in work:
        if v % 4 != 0:
            print('No')
            exit()
    print('Yes')

four_elements_cnt = (W // 2) * (H // 2)
now_2 = 0
now_4 = 0
if H % 2 == 0 or W % 2 == 0:
    if H % 2 == 0:
        two_elements_cnt = H // 2
    else:
        two_elements_cnt = W // 2

    for v in counter.values():
        if v % 4 == 0:
            now_4 += v // 4
        elif v % 2 == 0:
            now_4 += v // 4
            now_2 += 1
        else:
            print('No')
            exit()
    if now_4 >= four_elements_cnt and now_2 == (now_4 - four_elements_cnt) * 2 + now_2:
        print('Yes')
    else:
        print('No')

one_elements_cnt = 1
now_1 = 0
if H % 2 == 1 and W % 2 == 1:
    two_elements_cnt = (H // 2) + (W // 2)
    for v in counter.values():
        if v % 4 == 0:
            now_4 += v // 4
        elif v % 2 == 0:
            now_4 += v // 4
            now_2 += 1
        else:
            now_4 += v // 4
            now_2 += (v // 4) //2
            now_1 += 1
    if now_4 >= four_elements_cnt and now_2 <= (now_4 - four_elements_cnt) * 2 + now_2 and one_elements_cnt == now_1 + now_2 + (now_4 - four_elements_cnt) * 2 - two_elements_cnt:
        print('Yes')
    else:
        print('No')