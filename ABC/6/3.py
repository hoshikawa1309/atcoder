N, M = map(int, input().split())
for adult in range(N + 1):
    old = 4 * N - M - 2 * adult
    baby = adult + M - 3 * N
    if adult + old + baby == N and adult * 2 + old * 3 + baby * 4 == M and \
            adult >= 0 and baby >= 0 and old >= 0:
        print(adult, old, baby)
        exit()

print("-1 -1 -1")