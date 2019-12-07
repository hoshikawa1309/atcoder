S = list(input())
lenS = len(S)
T = list(input())
lenT = len(T)
Flag = False
for i in range(lenS - lenT, -1 , -1):
    for j in range(lenT - 1, -1 , -1):
        if S[i + j] != "?" and T[j] != S[i + j]:
            break
    else:
        Flag = True
        for j in range(lenT - 1 , -1 , -1):
            S[i + j] = T[j]
        break
if Flag:
    for i in range(lenS):
        if S[i] == "?":
            S[i] = "a"
    print("".join(S))
else:
    print("UNRESTORABLE")