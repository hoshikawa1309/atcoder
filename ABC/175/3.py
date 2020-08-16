X, K, D = map(int, input().split())
negative = False
if X < 0:
    X = -X
    negative = True
cnt = X // D
if cnt >= K:
    print(abs(X - D * K))
    exit()
K -= cnt
X = X - D * cnt

if K % 2 == 0:
    print(abs(X))
else:
    print(abs(X - D))


