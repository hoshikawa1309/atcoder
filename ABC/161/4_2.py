K = int(input())
runrun = 0
for i in range(1, 1000000):
    str_i = str(i)
    now = int(str_i[0])
    for j in str_i:
        if abs(now - int(j)) > 1:
            break
    else:
        runrun += 1
    if runrun == K:
        print(i)
        exit()
