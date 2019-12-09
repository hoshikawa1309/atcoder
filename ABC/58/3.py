from collections import Counter
N = int(input())
S = []
for _ in range(N):
    s = list(input())
    s.sort()
    S.append(s)
S = Counter(S)
S_key =
char_num = ord("a")
for i in range(26):
    flag = True
    for j in range(N):
        for key , val in S[j]:
            if key == chr(char_num + i):

