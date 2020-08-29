s = input()
len_s = len(s)
N = int(input())
print(s)
ans = [s]
for _ in range(N):
    t = input()
    len_t = len(input())
    flag = False
    for i in range(len_s):
        for j in range(len_t):
            if t[j] == '*':
                continue
            if len_t + s <= len_s or t[j] != s[i + j]:
                break
        else:

            flag = True
    if flag:
        ans.append('*' * len_t)
    else:
        ans.

