N = int(input())
S = input()
ans = 0
for s in S:
    if s == 'A':
        ans += 4
    elif s == 'B':
        ans += 3
    elif s == 'C':
        ans += 2
    elif s == 'D':
        ans += 1
print(ans / N)