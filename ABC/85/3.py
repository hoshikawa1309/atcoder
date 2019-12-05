N ,Y = map(int,input().split())
for k10 in range(N + 1):
    for k5 in range(N - k10 + 1):
        k1 = (Y - (k10 * 10000 + k5 * 5000)) / 1000
        if k1.is_integer() and k1 + k5 + k10 == N:
            print(k10, k5, int(k1))
            exit()
print("-1 -1 -1")
