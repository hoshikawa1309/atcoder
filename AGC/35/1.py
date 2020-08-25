from collections import Counter
N = int(input())
A = Counter(map(int, input().split()))
tmp1 = list(A.items())
tmp1.sort()
if len(tmp1) == 1 and tmp1[0][0] == 0 or len(tmp1) == 2 and tmp1[0][0] == 0 and tmp1[1][1] == N // 3 * 2 and tmp1[0][1] == N // 3 or len(tmp1) == 3 and (tmp1[0][0] ^ tmp1[1][0] ^ tmp1[2][0]) == 0 and tmp1[0][1] == tmp1[1][1] == tmp1[2][1] == N // 3:
    print('Yes')
else:
    print('No')


