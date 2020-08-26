s, t = input().split()
a, b = map(int,input().split())
U = input()
d = {s: a, t: b}
if U == s:
    print(a - 1, b)
else:
    print(a, b - 1)