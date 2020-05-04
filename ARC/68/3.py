x = int(input())
# mod = 10 ** 9 + 7
tmp = x // 11
nokori = x % 11
if nokori == 0:
    print(tmp * 2)
elif nokori > 6:
    print(tmp * 2 + 2)
else:
    print(tmp * 2 + 1)