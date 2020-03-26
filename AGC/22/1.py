S = input()
if S == "zyxwvutsrqponmlkjihgfedcba":
    print("-1")
    exit()

if len(S) < 26:
    for i in range(26):
        if not chr(ord("a") + i) in S:
            print(S + chr(ord("a") + i))
            exit()
else:
    pop_list = []
    S = list(S)
    while True:
        pop_chr = S.pop()
        pop_list.append(pop_chr)
        pop_list.sort()
        for candidate in pop_list:
            if S[-1] < candidate:
                S.pop()
                S.append(candidate)
                print(*S, sep="")
                exit()
