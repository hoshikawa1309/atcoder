S = list(input().split())
ans_set = set()
for s in S:
    username = ''
    for i in range(len(s) - 1,-1 ,-1):
        c = s[i]
        if c == '@':
            if username:
                ans_set.add(username)
            username = ''
        else:
            username = c + username
ans = list(ans_set)
ans.sort()
if ans:
    for a in ans:
        print(a)
