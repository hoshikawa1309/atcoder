from collections import Counter
S = list(input())
S = Counter(S)
S = list(S.keys())
S.sort()
for i in range(26):
    alph = chr(ord("a") + i)
    #print(alph)
    if i == len(S):
        print(chr(ord("a") + i))
        exit()
    elif S[i] != chr(ord("a") + i):
        print(alph)
        exit()

print("None")


