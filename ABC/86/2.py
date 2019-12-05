a, b = input().split()
c = a + b
c = int(c) ** (1 / 2)
print("Yes" if c.is_integer() else "No")
