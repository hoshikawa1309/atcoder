s = input()
g_cnt = 0
p_cnt = 0
for c in s:
    if c == 'g':
        g_cnt += 1
    else:
        p_cnt += 1
print((g_cnt - p_cnt) // 2)