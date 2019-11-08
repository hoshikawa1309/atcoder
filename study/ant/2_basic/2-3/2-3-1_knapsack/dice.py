from pprint import pprint
N , D = map(int,input().split())

count_2 = 0
count_3 = 0
count_5 = 0

for i in range(70):
    if D % 2 == 0:
        D = D // 2
        count_2 += 1
    else:
        break

for j in range(50):
    if D % 3 == 0:
        D = D // 3
        count_3 += 1
    else:
        break

for k in range(40):
    if D % 5 == 0:
        D = D //5
        count_5 += 1
    else:
        break
if D != 1:
    print("0")
    exit()

dp = [[[[0 for _ in range(count_5 + 1)] for _ in range(count_3 + 1)] for _ in range(count_2 + 1)] for _ in range(N + 1)]
dp[0][0][0][0] = 1
for n in range(N):
    for i in range(count_2 + 1):
        for j in range(count_3 + 1):
            for k in range(count_5 + 1):
                for x in  range(6):
                    a = (dp[n][i][j][k]) / 6
                    if x == 1:
                        dp[n+1][i][j][k] += a
                    elif x == 2:
                        d = min(i+1,count_2)
                        dp[n+1][d][j][k] += a
                    elif x == 3:
                        d = min(j + 1 , count_3)
                        dp[n + 1][i][d][k] += a
                    elif x == 4:
                        d = min(i+2 , count_2)
                        dp[n+1][d][j][k] += a
                    elif x == 5:
                        d = min(k + 1,count_5)
                        dp[n+1][i][j][d] += a
                    else:
                        d = min(i+1,count_2)
                        e = min(j + 1,count_3)
                        dp[n+1][d][e][k] += a
print(dp[N][count_2][count_3][count_5])
pprint(dp)
