N = int(input())
flags = []
for _ in range(N):
    d1, d2 = map(int, input().split())
    flags.append(d1 == d2)
#print(flags)
for i in range(N - 2):
    if flags[i] and flags[i + 1] and flags[i + 2]:
        print('Yes')
        exit()
print('No')