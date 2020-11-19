N = int(input())
scores = [int(input()) for _ in range(N)]
scores.sort(reverse=True)
Q = int(input())
capacity = [int(input()) for _ in range(Q)]
if len(set(scores)) == 1 and scores[0] == 0:
    for _ in range(Q):
        print(0)
    exit()
for c in capacity:
    if c == 0:
        print(scores[0] + 1)
    elif scores[c] == 0:
        print(0)
    elif scores[c - 1] == scores[c]:
        print(scores[c - 1] + 1)
    else:
        print(scores[c - 1])
