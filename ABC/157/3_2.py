N, M = map(int, input().split())
sc = list(list(map(int, input().split())) for _ in range(M))

for i in range(1000):
    str_num = str(i)
    num_len = len(str_num)
    if num_len != N:
        continue
    for s, c in sc:
        if num_len < s:
            break
        if int(str_num[s - 1]) != c:
            break
    else:
        print(i)
        exit()

print("-1")
