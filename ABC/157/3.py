N , M = map(int,input().split())
sc = list(tuple(map(int,input().split())) for _ in range(M))

for i in range(1000):
    num = []
    str_i = str(i)
    len_i = len(str_i)
    if len_i >= 3:
        num.append(int(str_i[-3]))
    else:
        num.append("")

    if len_i >= 2:
        num.append(int(str_i[-2]))
    else:
        num.append("")

    num.append(int(str_i[-1]))

    bad_flag = False
    for s, c in sc:
        if num[s - 1] != c:
            bad_flag = True
        if bad_flag:
            continue
    if not bad_flag:
        ans = i
        break

if bad_flag:
    print("-1")
else:
    print(ans)

