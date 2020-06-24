N, M = map(int, input().split())
AC_flags = [False] * N
WA_counter = [0] * N
for _ in range(M):
    p, s = input().split()
    p = int(p) - 1
    if AC_flags[p]:
        continue
    elif s == 'WA':
        WA_counter[p] += 1
    else:
        AC_flags[p] = True
penalty = 0
for i in range(N):
    penalty += AC_flags[i] * WA_counter[i]
print(sum(AC_flags), penalty)




