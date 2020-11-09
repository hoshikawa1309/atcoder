import bisect
N, M = map(int, input().split())
X = list(map(int, input().split()))
W = list(map(int, input().split()))
X.sort()

from_left_to_right = [0] * (N + 1)
from_right_to_left = [0] * (N + 1)
for i in range(2, N + 1, 2):
    from_left_to_right[i] = from_left_to_right[i - 2] + X[i - 1] - X[i - 2]
    from_left_to_right[i + 1] = from_left_to_right[i - 2] + X[i - 1] - X[i - 2]
    from_right_to_left[N - i] = from_right_to_left[N - i + 2] + X[N - i + 1] - X[N - i]
    from_right_to_left[N - i - 1] = from_right_to_left[N - i + 2] + X[N - i + 1] - X[N - i]
ans = float('inf')
for w in W:
    idx = bisect.bisect_left(X, w)
    # print(idx)
    if idx % 2 == 0:
        tmp_ans = (X[idx] - w) + from_right_to_left[idx] + from_left_to_right[idx]
    else:
        tmp_ans = (w - X[idx - 1]) + from_right_to_left[idx] + from_left_to_right[idx]
    # print(tmp_ans)
    ans = min(ans, tmp_ans)


# print(from_left_to_right)
# print(from_right_to_left)
print(ans)