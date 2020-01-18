S = list(input())
S = S[::-1]
exist = [[S[0]]]
work = []
now_idx = 0
for i in range(1,len(S)):
    work.extend(S[i])
    if work != exist[now_idx]:
        exist.append(work)
        work = []
        now_idx += 1
print(len(exist))