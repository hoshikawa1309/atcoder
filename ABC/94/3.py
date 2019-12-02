N = int(input())
X = list(map(int,input().split()))
X_work = sorted(X)
before = X_work[N // 2]
after = X_work[N // 2 - 1]
for x in X:
    if x <= after:
        print(before)
    else:
        print(after)