import math
A = list(map(int,input().split()))
A.sort(reverse=True)
cnt1 = (A[0] - A[1]) / 2
cnt2= (A[0] - A[2]) / 2
#print(cnt1)
#print(cnt2)
d1 ,i1 = math.modf(cnt1)
d2 ,i2 = math.modf(cnt2)

if d1 + d2 == 1:
    both_increase = 1
elif d1 + d2 == 0.5:
    both_increase = 2
else:
    both_increase = 0
print(int(i1 + i2 + both_increase))

