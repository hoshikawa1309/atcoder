K = int(input())
runrun = 0
num = 1
while runrun < K:
    s = str(num)
    len_str = len(s)
    if len_str == 1:
        runrun += 1
        num += 1
    else:
        for i in range(len_str - 1):
            if abs(int(s[i]) - int(s[i + 1])) > 1:
                num += 1
                break
        else:
            runrun += 1
            num += 1
print(num - 1)