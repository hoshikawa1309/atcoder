import bisect
N, T = map(int, input().split())
A = list(map(int, input().split()))
A_first = A[:N // 2]
A_second = A[N // 2:]
A_first_comb = []
A_second_comb = []
for i in range(2 ** len(A_first)):
    now = 0
    for j in range(len(A_first)):
        if i >> j & 1:
            now += A_first[j]
    A_first_comb.append(now)

for i in range(2 ** len(A_second)):
    now = 0
    for j in range(len(A_second)):
        if i >> j & 1:
            now += A_second[j]
    A_second_comb.append(now)
A_second_comb.sort()

# print(A_first_comb)
# print(A_second_comb)
ans = 0
for a in A_first_comb:
    if a > T:
        continue
    idx = min(bisect.bisect_left(A_second_comb, T - a), len(A_second_comb) - 1)

    if T - a >= A_second_comb[idx]:
        ans = max(ans, a + A_second_comb[idx])
    else:
        ans = max(ans, a + A_second_comb[idx - 1])
print(ans)