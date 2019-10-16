s = int(input())
lst = []
i = 1
while True:
    i += 1
    lst.append(s)
    if s % 2 == 0:
        s //= 2
    else:
        s = s * 3 + 1

    if s in lst:
        break
print(i)