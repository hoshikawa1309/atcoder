N = int(input())
NGword = []
for _ in range(3):
    NGword.append(int(input()))

if N in NGword:
    print("NO")
    exit()
for count in range(101):
    print(N)
    if N == 0:
        print("YES")
        exit()
    if not N - 3 in NGword and N >= 3:
        N -= 3
    elif not N - 2 in NGword and N >= 2:
        N -= 2
    elif not N - 1 in NGword and N >= 1:
        N -= 1
    if count == 100:
        print("NO")
        exit()
