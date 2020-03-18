N = input()
i_N = 0
for i in range(len(N)):
    i_N += int(N[i])
if len(N) == 1:
    print(N)
    exit()
ans = (len(N) - 1) * 9
if N[0] != '9':
    ans += int(N[0]) - 1
else:
    for i in range(1, len(N)):
        if N[i] != '9':
            ans += int(N[i - 1]) - 1
            break
    else:
        ans += 9
if ans > i_N:
    print(ans)
else:
    print(i_N)
