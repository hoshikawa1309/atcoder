n, m = map(int, input().split())
n %= 12
long = n * 30 + 0.5 * m
short = 6 * m
print(min(abs(long - short), 360 - abs(long - short)))