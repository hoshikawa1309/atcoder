c = input()
ans = ''
flag = False
for i in range(len(c)):
    if ' ' == c[i]:
        flag = True
        continue
    if flag:
        ans += ','
        ans += c[i]
        flag = False
    else:
        ans += c[i]
print(ans)