X = int(input())
ans = 0
ans += (X // 500) * 1000
X %= 500
ans += (X // 5) * 5
print(ans)