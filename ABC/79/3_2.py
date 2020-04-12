S = list(input())
opt = ['-', '+']
for i in range(8):
    now = S[0]
    for j in range(3):
        if i >> j & 1:
            now += opt[1]
        else:
            now += opt[0]
        now += S[j + 1]
    if eval(now) == 7:
        print(now + "=7")
        exit()

