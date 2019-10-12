N = int(input())
ans = 0
money = []
for _ in range(N):
    x , u = input().split()
    money.append([float(x) , u])

for i in range(N):
    if money[i][1] == "JPY":
        ans += money[i][0]
    else:
        ans += money[i][0] * 380000.0
print(ans)