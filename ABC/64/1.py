r, g, b = map(int, input().split())
num = r * 100 + g * 10 + b
print('YES' if num % 4 == 0 else 'NO')