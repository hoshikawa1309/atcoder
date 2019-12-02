from collections import Counter
N = int(input())
S = list(input())
S_C = Counter(S)
left_num = S_C["E"]
if S[0] == "E":
    left_num -= 1
right_num = 0
ans = left_num + right_num
for i in range(1,N):
    # リーダーが左を向いていた時、-1
    if S[i] == "E":
        left_num -= 1
    if S[i-1] == "W":
        right_num += 1
    tmp_ans = left_num + right_num
    if ans > tmp_ans:
        ans = tmp_ans
print(ans)