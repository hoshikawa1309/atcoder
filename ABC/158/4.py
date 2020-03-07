from collections import deque
S = deque(input())
Q = int(input())
inversion_flag = False
for _ in range(Q):
    query_list = list(input().split())
    if query_list[0] == "1":
        inversion_flag = not inversion_flag
        continue
    C = query_list[2]
    if query_list[1] == "2":
        if inversion_flag:
            S.appendleft(C)
        else:
            S.append(C)
    else:
        if inversion_flag:
            S.append(C)
        else:
            S.appendleft(C)

S = list(S)
if inversion_flag:
    print(*S[::-1], sep="")
else:
    print(*S, sep="")
