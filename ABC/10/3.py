import math
txa ,tya, txb , tyb, T , V = map(int,input().split())
n = int(input())
girls = [list(map(int,input().split())) for _ in range(n)]
now_x , now_y = txa , tya
distance = 0
for i in range(n):
    distance += math.sqrt((girls[i][0] - now_x ) ** 2 + (girls[i][1] - now_y) ** 2 )
    now_x , now_y = girls[i][0] , girls[i][1]
distance += math.sqrt((now_x - txb) ** 2 + (now_y - tyb) ** 2 )
print(distance)
print(T * V)
if distance <= T * V:
    print("YES")
else:
    print("NO")
