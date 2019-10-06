S = list(input())
K = int(input())
# S = list("ccccc")
# K = 3
# S = list("aabca")
# K = 2
if S.count(S[0]) == len(S):
    print(len(S) * K // 2)
    exit()

cnt = 0
continuous = 0
chr = S[0]
for i in range(1, len(S)):
    if chr == S[i]:
        cnt += 1
    if chr != S[i] or i == len(S) - 1:
        continuous += (cnt + 1) // 2
        cnt = 0
    chr = S[i]
chr = S[0]
left = 0
idx = 0
while idx < len(S) and S[idx] == chr:
    left += 1
    idx += 1
idx = -1
right = 0
while idx < len(S) and S[idx] == chr:
    right += 1
    idx -= 1
same = right + left
if continuous == 0 and S[0] == S[-1]:
    print(K - 1)
else:
    ans = K * continuous
    if S[0] == S[-1]:
        ans += left // 2 + (left + right) // 2 * (K - 1) + right // 2
    else:
        ans += (left // 2 + right // 2) * K
    print(ans)