import math
import bisect
def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

Q = int(input())
lr_list = [list(map(int,input().split())) for _ in range(Q)]
flags = [False] * (10 ** 5)


for i in range(1, 10 ** 5 + 1, 2):
    if not flags[i]:
        flag1 = is_prime(i)
        flag2 = is_prime((i + 1) // 2)
        if flag1 and flag2:
            flags[i] = True
True_idxs = []
for i in range(len(flags)):
    if flags[i]:
        True_idxs.append(i)

# print(True_idxs)

for l, r in lr_list:
    l_idx = bisect.bisect_left(True_idxs, l)
    r_idx = bisect.bisect_right(True_idxs, r)
    print(r_idx - l_idx)