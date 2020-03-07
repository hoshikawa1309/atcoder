S = list(input())
T = list(input())
len_T = len(T)
for _ in range(len_T):
    if S == T:
        print("Yes")
        exit()
    else:
        tmp = T.pop(0)
        T.append(tmp)
print("No")
