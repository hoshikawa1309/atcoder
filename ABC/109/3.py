import bisect
def gcd(x , y):
    max_val = max(x , y)
    min_val = min(x , y)
    while min_val != 0:
        max_val , min_val = min_val , max_val % min_val
    return max_val
N , X = map(int,input().split())
x = list(map(int,input().split()))
x.sort()
split_idx = bisect.bisect_left(x , X)
BeforeList = x[:split_idx]
AfterList = x[split_idx:]
now = X
ans = 0
DistanceList = []
for val in AfterList:
    distance = abs(val - now)
    DistanceList.append(distance)
    now = val
for val in BeforeList:
    distance = abs(val - now)
    DistanceList.append(distance)
    now = val

ans = DistanceList[0]
for i in range(1,len(DistanceList)):
    ans = gcd(DistanceList[i] , ans)
print(ans)