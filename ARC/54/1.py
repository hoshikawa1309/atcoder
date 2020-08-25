L, X, Y, S, D = map(int, input().split())
if Y <= X:
    if Y != X:
        print(min(abs(S - D) / abs(X + Y), abs(L - abs(S - D)) / abs(Y - X)))
    else:
        print(abs(S - D) / (X + Y))
else:
    if Y != X:
        print(min(abs(S - D) / abs(Y - X), abs(L - abs(S - D)) / (Y + X)))
    else:
        print(abs(L - abs(S - D)) / (Y + X))