x = int(input())
ans = x // 11 * 2
nokori = x % 11
if nokori > 6:
    print(ans + 2)
elif nokori == 0:
    print(ans)
else:
    print(ans + 1)