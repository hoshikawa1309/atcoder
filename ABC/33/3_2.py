S = list(input().split('+'))
ans = 0
for formula in S:
    if not '0' in formula:
        ans += 1
print(ans)