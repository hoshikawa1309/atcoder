from collections import Counter
N = int(input())
S = Counter(input() for _ in range(N))
S = S.most_common()
most_count = S[0][1]
S.sort()
for i in range(len(S)):
    if S[i][1] == most_count:
        print(S[i][0])
