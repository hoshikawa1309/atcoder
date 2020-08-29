from collections import defaultdict
N = int(input())
D = list(map(int, input().split()))
D_dict = defaultdict(int)
for d in D:
    D_dict[d] += 1
M = int(input())
T = list(map(int, input().split()))
T_dict = defaultdict(int)
for t in T:
    T_dict[t] += 1

for target, t_cnt in T_dict.items():
    d_cnt = D_dict[target]
    if t_cnt > d_cnt:
        print('NO')
        exit()
print('YES')