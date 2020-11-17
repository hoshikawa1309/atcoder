H, W, M = map(int, input().split())
h_cnt = [0] * (H + 1)
h_list = []
w_cnt = [0] * (W + 1)
w_list = []
s = set()
for _ in range(M):
    h, w = map(int, input().split())
    h_list.append(h)
    h_cnt[h] += 1
    w_list.append(w)
    w_cnt[w] += 1
    s.add((h, w))

h_cnt_max =max(h_cnt)
h_idx_list = []
for idx, h in enumerate(h_cnt):
    if h_cnt_max == h:
        h_idx_list.append(idx)


w_cnt_max = max(w_cnt)
w_idx_list = []
for idx, w in enumerate(w_cnt):
    if w_cnt_max == w:
        w_idx_list.append(idx)


for h in h_idx_list:
    for w in w_idx_list:
        if (h, w) in s:
            continue
        print(h_cnt_max + w_cnt_max)
        exit()
print(h_cnt_max + w_cnt_max - 1)


