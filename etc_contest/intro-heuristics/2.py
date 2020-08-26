D = int(input())
c = list(map(int, input().split()))
scores = []
for _ in range(D):
    scores.append(list(map(int, input().split())))

for i in range(D):
    t = int(input())
    print(scores[i][t])

