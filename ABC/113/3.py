N , M = map(int,input().split())
birth = []
for i in range(M):
    a , b = map(int,input().split())
    birth.append([a,b,i])
#print(birth)
work_list = sorted(birth,key=lambda x: x[1])
work_list.sort()
#print(birth)
lower = 1
ans = []
for i in range(1,len(birth)):
    ans.append([work_list[i-1][2],str(work_list[i-1][0]).zfill(6) + str(lower).zfill(6)])
    if work_list[i][0] == work_list[i-1][0]:
        lower += 1
    else:
        lower = 1
ans.append([work_list[M - 1][2],str(work_list[M-1][0]).zfill(6) + str(lower).zfill(6)])
ans.sort()
for val in ans:
    print(val[1])
