S = list(input())
ans = 0
i = 0
cnt = 0
lst = ["A","C","G","T"]
for c in S:
    if c in lst:
        cnt += 1
    else:
        if ans < cnt:
            ans = cnt
        cnt = 0
if ans < cnt:
    ans = cnt
print(ans)