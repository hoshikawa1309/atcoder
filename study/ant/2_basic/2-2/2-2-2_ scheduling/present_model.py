import bisect

def LIS(L):
    dp = [L[0]]
    for i in L:
        if i > dp[-1]:
            dp.append(i)
        else:
            dp[bisect.bisect_left(dp,i)] = i
    return len(dp)


N = int(input())
presents = [list(map(int,input().split())) for _ in range(N)]
presents.sort(key = lambda x: (x[0] ,-x[1]))

print(LIS([row[1] for row in presents]))