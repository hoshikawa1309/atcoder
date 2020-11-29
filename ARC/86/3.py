from collections import Counter
N, K = map(int, input().split())
A = list(map(int ,input().split()))
A_counter = Counter(A)
cnt_list = list(A_counter.values())
cnt_list.sort(reverse=True)
ans = 0
for i, cnt in enumerate(cnt_list):
    if i >= K:
        ans += cnt
print(ans)