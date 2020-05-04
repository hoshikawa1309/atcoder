N = int (input())
work = []
work_time = 0
flag = 0

for i in range(N):
    work.append(list(map(int , input().split())))
#print(work)
work = sorted(work , key = lambda x: x[1])
#work.sort()
#sort(work)
#print()
#print("sorting ... ")
#print()
#print(work)
for i in range(N):
    work_time += work[i][0]
    if work_time > work[i][1]:
        flag = 1
        break

if flag == 1:
    print('No')
else:
    print('Yes')
