X , Y = map(int,input().split())
if X == Y == 1:
    print("1000000")
    exit()
point = 0
if X == 1:
    point += 300000
elif X == 2:
    point += 200000
elif X == 3:
    point += 100000

if Y == 1:
    point += 300000
elif Y == 2:
    point += 200000
elif Y == 3:
    point += 100000
print(point)