n = int(input())
x = list(map(int, input().split()))
m = 0
y = 0
c = abs(x[0])
for xi in x:
    m += abs(xi)
    y += abs(xi) ** 2
    c = max(c, abs(xi))
print(m)
print(y ** (1 / 2))
print(c)
