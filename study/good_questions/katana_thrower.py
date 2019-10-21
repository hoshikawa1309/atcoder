import math
N , H = map(int , input().split())
slash = []
throw = []
for _ in range(N):
    a , b = map(int , input().split())
    slash.append(a)
    throw.append(b)
count = 0
#print(slash)
slash_max = max(slash)
#print(throw)
throw.sort(reverse = True)
#print(throw)
while H > 0:
    #print(H)
    if not throw or throw[0] < slash_max :
        count += math.ceil(H / slash_max)
        break
    else:
        H -= throw[0]
        throw.pop(0)
        #print(throw)
    count += 1
print(count)
