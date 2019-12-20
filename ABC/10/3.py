import math
txa ,tya, txb , tyb, T , V = map(int,input().split())
n = int(input())
girls = [list(map(int,input().split())) for _ in range(n)]
Flag =False
now_x , now_y = txa , tya
distance = 0
for i in range(n):
    distance = math.sqrt((girls[i][0] - txa) ** 2 + (girls[i][1] - tya) ** 2 )
    distance += math.sqrt((girls[i][0] - txb) ** 2 + (girls[i][1] - tyb) ** 2 )
    if distance <= T * V:
        Flag = True
        break
if Flag:
    print("YES")
else:
    print("NO")
