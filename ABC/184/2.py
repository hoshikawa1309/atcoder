N, X = map(int, input().split())
S = input()
for c in S:
    if c == 'o':
        X += 1
    else:
        X = max(X - 1, 0)
print(X)