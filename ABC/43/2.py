S = input()
ans = []
for s in S:
    if s == "B":
        if ans:
            ans.pop(-1)
    else:
        ans.append(s)
print(*ans, sep='')