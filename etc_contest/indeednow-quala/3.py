N = int(input())
scores = []
for _ in range(N):
    score = int(input())
    if score:
        scores.append(score)

scores.sort(reverse=True)

Q = int(input())
for _ in range(Q):
    k = int(input())
    if k < len(scores):
        print(scores[k] + 1)
    else:
        print('0')
