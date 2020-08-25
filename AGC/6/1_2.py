N = int(input())
s = input()
t = input()
ans = s
for i in range(N + 1):
    tmp_ans = s + t[i:]
    # print(tmp_ans)
    if tmp_ans[:N] == s and tmp_ans[-N:] == t:
        ans = tmp_ans
print(len(ans))
