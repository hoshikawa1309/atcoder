N = int(input())
scores = []
for _ in range(N):
    x = int(input())
    if x:
        scores.append(x)
scores.sort(reverse=True)
Q = int(input())
for _ in range(Q):
    capacity = int(input())
    if capacity >= len(scores):
        print(0)
    else:
        print(scores[capacity] + 1)
