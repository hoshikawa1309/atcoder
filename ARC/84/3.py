from bisect import bisect_right
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort()
B.sort()
C.sort()

comb = [0] * N

# まずは中段、下段のみをかんがえる
for idx, val in enumerate(B):
    c_idx = bisect_right(C, val)
    comb[idx] += N - c_idx

# print(comb)
ans = 0
s = [0] * N
s[-1] = comb[-1]
for i in range(N - 2, -1, -1):
    s[i] = s[i + 1] + comb[i]
# print(s)
for idx, val in enumerate(A):
    b_idx = bisect_right(B, val)
    if b_idx == N:
        continue
    # print(b_idx)
    ans += s[b_idx]
print(ans)