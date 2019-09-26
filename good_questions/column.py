'''
N = int(input())
list = [int(i) for i in input().split()]
list = list[::-1]
#print(list)
current_column = 0
cost = 0
while current_column < N - 1:
    #print(current_column)
    if N - 2 - current_column == 0:
        cost += abs(list[current_column] - list[current_column + 1])
        break
    if N - 3 - current_column == 0:
        cost += abs(list[current_column] - list[current_column + 2])
        break
    sa1 = abs(list[current_column] - list[current_column + 1])
    sa2 = abs(list[current_column] - list[current_column + 2])
    if sa1 >= sa2:
        cost += sa2
        current_column += 2
    else:
        cost += sa1
        current_column += 1
print(cost)
'''

N = int(input())
list = [int(i) for i in input().split()]
INF = float("inf")
dp = [INF] * N
dp[0] = 0
dp[1] = abs(list[1] - list[0])
for i in range(2,N):
    dp[i] = min(dp[i - 2] + abs(list[i] - list[i - 2]),dp[i - 1] + abs(list[i] - list[i - 1]))
print(dp[N - 1])
