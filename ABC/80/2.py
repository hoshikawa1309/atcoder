def digit_sum(n):
    n = str(n)
    S = list(map(int,n))
    return sum(S)

X = int(input())
fX = digit_sum(X)
print("Yes" if X % fX == 0 else "No")