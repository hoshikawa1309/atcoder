N = int(input())
rate = [False] * 8
a = list(map(int,input().split()))
a.sort()
CntOver3200 = 0

for i in range(N):
    if a[i] >= 3200:
        CntOver3200 = N - i
        break
    rate[a[i] // 400] = True
min_val = max(sum(rate) , 1)
if any(rate):
    max_val = min_val + CntOver3200
else:
    max_val = CntOver3200
print(min_val , max_val)