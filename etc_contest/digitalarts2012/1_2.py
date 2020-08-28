s = input().split()
len_s = len(s)
ans = list(s)
N = int(input())
for _ in range(N):
    t = input()
    len_t = len(t)
    for i in range(len_s):
        string = s[i]
        if len(string) != len_t:
            continue
        for j in range(len_t):
            if t[j] != string[j] and t[j] != '*':
                break
        else:
            ans[i] = '*' * len_t
print(*ans)