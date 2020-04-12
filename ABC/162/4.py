import bisect
N = int(input())
S = input()
if not 'R' in S and 'G' in S and 'B' in S:
    print("0")
    exit()
R_idx_list = []
G_idx_list = []
B_idx_list = []
for i in range(len(S)):
    if S[i] == 'R':
        R_idx_list.append(i)
    elif S[i] == 'G':
        G_idx_list.append(i)
    else:
        B_idx_list.append(i)

ans = 0
for i in range(len(S) - 2):
    rgb_flags = [False] * 3
    i_chr = S[i]
    if i_chr == 'R':
        rgb_flags[0] = True
    elif i_chr == 'G':
        rgb_flags[1] = True
    elif i_chr == 'B':
        rgb_flags[2] = True
    for j in range(i + 1, len(S) - 1):
        j_chr = S[j]
        if i_chr == j_chr:
            continue
        if j_chr == 'R':
            rgb_flags[0] = True
        elif j_chr == 'G':
            rgb_flags[1] = True
        elif j_chr == 'B':
            rgb_flags[2] = True
        num = (j - i) * 2
        if not rgb_flags[0] and j < R_idx_list[-1]:
            r_idx = bisect.bisect_right(R_idx_list, j)
            ans += len(R_idx_list) - r_idx
            idx = bisect.bisect_left(R_idx_list, num)
            if len(R_idx_list) > idx and R_idx_list[idx] - j == j - i:
                ans -= 1

        if not rgb_flags[1] and j < G_idx_list[-1]:
            g_idx = bisect.bisect_right(G_idx_list, j)
            ans += len(G_idx_list) - g_idx
            idx = bisect.bisect_left(G_idx_list, num)
            if len(G_idx_list) > idx and G_idx_list[idx] - j == j - i:
                ans -= 1

        if not rgb_flags[2] and j < B_idx_list[-1]:
            b_idx = bisect.bisect_right(B_idx_list, j)
            ans += len(B_idx_list) - b_idx
            idx = bisect.bisect_left(B_idx_list, num)
            if len(B_idx_list) > idx and B_idx_list[idx] - j == j - i:
                ans -= 1

        if j_chr == 'R':
            rgb_flags[0] = False
        elif j_chr == 'G':
            rgb_flags[1] = False
        elif j_chr == 'B':
            rgb_flags[2] = False
print(ans)