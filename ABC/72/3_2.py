import bisect
N = int(input())
A = list(map(int, input().split()))
A.sort()
ans = 0

for i in range(1, 100000):
    right_idx = bisect.bisect_left(A, i - 1)
    left_idx = bisect.bisect_right(A, i + 1)
    tmp_ans = left_idx - right_idx
    if tmp_ans > ans:
        ans = tmp_ans
print(ans)