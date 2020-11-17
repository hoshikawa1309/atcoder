s = input()
if len(set(s)) == 1:
    print(0)
    exit()

ori_s = s
ans = float('inf')
for c in set(ori_s):
    s = ori_s
    tmp_ans = 0
    while len(set(s)) > 1:
        work = ''
        for i in range(len(s) - 1):
            if s[i] == c or s[i + 1] == c:
                work += c
            else:
                work += s[i]
        s = work
        tmp_ans += 1
    ans = min(ans, tmp_ans)

print(ans)