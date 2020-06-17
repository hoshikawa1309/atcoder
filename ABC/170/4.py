N = int(input())
A = list(map(int, input().split()))
A.sort()
exist_flags = [0] * (10 ** 6)
for a in A:
    if exist_flags[a - 1] > 0:
        exist_flags[a - 1] += 1
    else:
        # for i in range(a, 25, a):
        for i in range(a, 10 ** 6 + 1, a):
            exist_flags[i - 1] += 1


ans = 0
for a in A:
    if exist_flags[a - 1] == 1:
        ans += 1
print(ans)