# 5000000000000000
S = list(input())
K = int(input())
for c in range(len(S)):
    if "1" == S[c] and c+1 < K:
        continue
    elif "1" == S[c] and c+1 <= K:
        print(1)
        exit()
    else:
        print(S[c])
        exit()