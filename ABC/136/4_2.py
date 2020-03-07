S = input()
len_S = len(S)
now = "R"
R_cnt = 0
L_cnt = 0
ans = [0] * len_S
R_idx_list = []
L_idx_list = []
for i in range(len_S - 1):
    if S[i] == "R" and S[i + 1] == "L":
        R_idx_list.append(i)
        L_idx_list.append(i + 1)


idx = 0
for i in range(len(S)):
    s = S[i]
    if i == len_S - 1:
        L_cnt += 1
    if now == "L" and s == "R" or i == len_S - 1:
        ans[R_idx_list[idx]] = R_cnt - R_cnt // 2 + L_cnt // 2
        ans[L_idx_list[idx]] = L_cnt - L_cnt // 2 + R_cnt // 2
        idx += 1
        R_cnt = 0
        L_cnt = 0
    if s == "R":
        now = "R"
        R_cnt += 1
    else:
        now = "L"
        L_cnt += 1
print(*ans)