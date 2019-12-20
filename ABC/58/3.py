from collections import Counter
N = int(input())
S = []
for _ in range(N):
    s = list(input())
    s.sort()
    S.append(s)

work = S[0]
for i in range(1 , N):
    work_lst = []
    while len(work) != 0 and len(S[i]) != 0:
        if work[0] == S[i][0]:
            c = S[i].pop(0)
            c = work.pop(0)
            work_lst.append(c)
        elif work[0] > S[i][0]:
            S[i].pop(0)
        elif work[0] < S[i][0]:
            work.pop(0)
    work = work_lst
if N == 1:
    print("".join(s))
else:
    print("".join(work_lst))


