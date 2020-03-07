S = input()
ans_list = [0] * (len(S) + 1)
for i in range(len(S)):
    if S[i] == '<':
        ans_list[i + 1] = ans_list[i] + 1

for i in range(len(S) - 1,-1,-1):
    if S[i] == '>':
        ans_list[i] = max(ans_list[i + 1] + 1, ans_list[i])

print(sum(ans_list))