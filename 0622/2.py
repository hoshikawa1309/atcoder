import copy
N,L = map(int,input().split())
flaver = []
for i in range(1,N + 1):
    flaver.append(L + i - 1)
flaver_sum = sum(flaver)
for i in range(len(flaver)):
    c_flaver = copy.deepcopy(flaver)
    del c_flaver[i]
    if i == 0:
        tmp_min = abs(flaver_sum - sum(c_flaver))
        index = i
    if abs(flaver_sum - sum(c_flaver)) < tmp_min:
        tmp_min = abs(flaver_sum - sum(c_flaver))
        index = i
del flaver[index]
print(sum(flaver))
