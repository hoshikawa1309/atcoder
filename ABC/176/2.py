N = input()
check = 0
for c in N:
    check += int(c)
    check %= 9
if check:
    print('No')
else:
    print('Yes')
