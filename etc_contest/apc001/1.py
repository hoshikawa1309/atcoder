a, b = map(int, input().split())
ans = -1
for i in range(1, 4):
  if a * i % b != 0:
    ans = a * i
print(ans)
