S = input()
for i in range(2 ** len(S) - 1):
    work = S
    for j in range(1 ,len(S)):
        if i >> (j - 1) & 1:
            work = work[:2 * j - 1] + "+" + work[2 * j - 1:]
        else:
            work = work[:2 * j - 1] + "-" + work[2 * j - 1:]
    if eval(work) == 7:
        print("{0}=7".format(work))
        exit()