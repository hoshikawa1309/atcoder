N = int(input())
s = input()
t = input()
s_one = s.count('1')
t_one = t.count('1')
if s == t:
    print(0)
    exit()
if s_one < t_one or s_one % 2 != t_one % 2:
    print(-1)
    exit()
s_one_idx = []
t_one_idx = []
s_cnt = 1
t_cnt = 1
for i in range(N - 1, -1, -1):
    if s[i] == '1':
        s_one_idx.append([s_cnt, i])
        s_cnt += 1
    if t[i] == '1':
        t_one_idx.append([t_cnt, i])
        t_cnt += 1

ans = 0
for i in range(len(t_one_idx)):
    s_num, s_idx = s_one_idx[i]
    t_num, t_idx = t_one_idx[i]
    if s_idx < t_idx:
        print(-1)
        exit()
    ans += s_idx - t_idx

for i in range(len(t_one_idx), len(s_one_idx)):
    _, s_idx = s_one_idx[i]
    ans += s_idx
print(ans)