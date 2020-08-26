from collections import Counter
N = int(input())
A = Counter(map(int, input().split()))
work = []
for key, val in A.items():
    while val > 2:
        val -= 2
    work.append(val)
len_work = len(work)
two_cnt = work.count(2)
if two_cnt % 2 == 0:
    print(len_work)
else:
    print(len_work - 1)