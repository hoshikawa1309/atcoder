N = int (input())
time = []
limit = []
work_time = 0
flag = 0

for i in range(N):
    A , B = map(int , input().split())
    time.append(A)
    limit.append(B)
#print(limit.index(min(limit)))
for i in range(N):
    work_time += time[limit.index(min(limit))]
    if work_time > max(limit):
        flag = 1
        break
    del limit[limit.index(min(limit))]
if flag == 1:
    print('No')
else:
    print('Yes')
