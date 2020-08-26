import copy
N = int(input())
X = list(map(int, input().split()))
tmp_X = copy.deepcopy(X)
tmp_X.sort()
m1 = tmp_X[N // 2]
m2 = tmp_X[N // 2 - 1]
for x in X:
    if x < m1:
        print(m1)
    else:
        print(m2)