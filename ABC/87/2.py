A = int(input())
B = int(input())
C = int(input())
X = int(input())
cnt = 0
for coin500 in range(A + 1):
    for coin100 in range(B + 1):
        for coin50 in range(C + 1):
            if coin50 * 50 + coin100 * 100 + coin500 * 500 == X:
                cnt += 1
print(cnt)