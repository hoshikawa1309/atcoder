a, b, x = map(int, input().split())
a_div = (a - 1) // x + 1
b_div = b // x + 1

print(b_div - a_div)