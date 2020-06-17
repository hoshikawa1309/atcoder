N = int(input())
enemy = list(map(int ,input().split()))
brave = list(map(int, input().split()))
enemy = enemy[::-1]
brave = brave[::-1]
sum = 0
for i in range(N):
    star = min(enemy[i] , brave[i])
    brave[i] = brave[i] - enemy[i]
    if brave[i] > 0:
        add_star = min(enemy[i + 1], brave[i])
        enemy[i+1] = enemy[i + 1] - add_star
        star += add_star
    sum+= star
print(sum)