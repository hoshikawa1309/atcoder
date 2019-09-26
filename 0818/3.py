N = int(input())
v = list(map(int , input().split()))
v = sorted(v)
ave = 0
for i in range(1,len(v)):
    if i == 1:
        sum = v[0] + v[1]
        ave = sum / 2
    else:
        ave = (ave + v[i]) / 2

print(ave)
