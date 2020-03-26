S = input()
ans = []
for s in S:
    if s == "0":
        ans.append(0)
    elif s == "1":
        ans.append(1)
    else:
        if ans:
            ans.pop(-1)
print(*ans, sep='')
