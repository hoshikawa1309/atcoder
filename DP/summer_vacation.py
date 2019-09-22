import sys
input = sys.stdin.readline
N = int(input())
work = []
num = [0,1,2]
for _ in range(N):
    a , b , c = map(int , input().split())
    work.append([a,b,c])
dp = [[0] * N for _ in range(3)]
for i in range(N):
    max_value = max(work[i])
    index = work[i].index(max_value)
    dp[i][index] = max_value
    dp[][] = 




