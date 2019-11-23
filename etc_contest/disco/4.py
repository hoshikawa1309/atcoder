from collections import Counter
M = int(input())
num = []
for _ in range(M):
    d , c = map(int,input().split())
    num.append([d,c])
#num = Counter(num)
i = 0
x , y = -1 , -1
while len(num) != 1 and num[0][1] != 1:
    if num[i][1] == 0:
        num.pop(0)
    else:
        x = num[i][0]
    if num[i][1] == 0:
        num.pop(0)
    else:
        y = num[i][0]
