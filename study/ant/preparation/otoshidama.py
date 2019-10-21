N , Y = map(int,input().split())
for k in range(N + 1):
    for k5 in range(N + 1):
        k10 = N - k - k5
        if k10 < 0:
            continue
        if 1000 * k + 5000 * k5 + 10000 * k10 == Y:
            print(k10, k5, k)
            exit()
print('-1 -1 -1')