N , D , K = map(int,input().split())
path = []
for i in range(D):
    l , r = map(int,input().split())
    path.append([l , r])
destination = []
for i in range(K):
    start, goal = map(int, input().split())
    if goal - start > 0:
        direction = 1
    else:
        direction = 0
    destination.append([start,goal,direction])
ans = []
for i in range(D):
    for j in range(K):
        if destination[j][2] == 1 and destination[j][0] >= destination[j][1] or  destination[j][2] == 0 and destination[j][1] >= destination[j][0]:
            continue
        now = destination[j][0]
        if min(path[i]) <= now <= max(path[i]):
            if destination[j][2] == 1:
                destination[j][0] = path[i][1]
            else:
                destination[j][0] = path[i][0]
        if destination[j][2] == 1 and destination[j][0] >= destination[j][1]:
            ans.append([j , i + 1])
        elif destination[j][2] == 0 and destination[j][1] >= destination[j][0]:
            ans.append([j , i + 1])
ans.sort()
for val in ans:
    print(val[1])