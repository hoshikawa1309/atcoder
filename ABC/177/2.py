S = input()
T = input()
ans = float('inf')
for i in range(len(S)):
    tmp_ans = 0
    for j in range(len(T)):
        if j + i >= len(S):
            break
        if S[i + j] != T[j]:
            tmp_ans += 1
    else:
        ans = min(ans, tmp_ans)
print(ans)