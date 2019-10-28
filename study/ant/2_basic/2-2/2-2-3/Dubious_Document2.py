s = list(input())
t = list(input())
flag = False
for j in range(len(s) - len(t) + 1):
    for i in range(1,len(t) + 2):
        if len(t) + 1 == i:
            flag = True
            start = len(s) - len(t) - j
            s = s[:start] + t + s[start + len(t):]
            break
        if s[-i - j] != "?" and t[-i] != s[-i - j]:
            break
    if flag:
        break
if flag:
    for i in range(len(s)):
        if s[i] == "?":
            s[i] = "a"
    print("".join(s))
else:
    print("UNRESTORABLE")