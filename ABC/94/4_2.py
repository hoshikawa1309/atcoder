import math
N = int(input())
A = list(map(int, input().split()))
A.sort()
ans = A[-1]
target = math.ceil(A[-1] / 2)
dis = float('inf')
for a in A:
    tmp_dis = abs(target - a)
    if tmp_dis < dis:
        dis = tmp_dis
        tmp_ans = a
print(ans, tmp_ans)

