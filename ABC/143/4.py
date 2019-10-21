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
N = int(input())
l = list(map(int,input().split()))
l.sort(reverse=True)
ans = 0
for i in range(N - 2):
    for j in range(i + 1,N - 1):
        for k in range(j + 1, N ):
            if l[i] < l[j] + l[k]:
                ans += 1
print(ans)
