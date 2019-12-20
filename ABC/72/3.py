from bisect import *
N = int(input())
a = list(map(int,input().split()))
a.sort()
ans = 0
min_a = min(a)
max_a = max(a)
for x in range(min_a , max_a + 1):
    r = bisect_right(a , x + 1)
    l = bisect_left(a , x - 1)
    tmp_max = r - l
    if tmp_max > ans:
        ans = tmp_max
print(ans)
