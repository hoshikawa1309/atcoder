C = int(input())
a = 1
b = 1
c = 1
for _ in range(C):
    l = list(map(int, input().split()))
    l.sort()
    a = max(a, l[0])
    b = max(b, l[1])
    c = max(c, l[2])
print(a * b * c)