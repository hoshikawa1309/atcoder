'''
import bisect
N = int(input())
l = list(map(int,input().split()))
l.sort()
#print(l)


ans = 0
for i in range(N - 1 , 1, -1):
    for j in range(i - 1 , 0 , -1):
        #work = l[:j]
        x = l[i] - l[j]
        #idx = bisect.bisect_right(work, x)
        idx = bisect.bisect_right(l, x)
        ans += max(j - idx , 0)
print(ans)
'''

