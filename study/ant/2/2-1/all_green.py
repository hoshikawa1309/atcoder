D , G = map(int,input().split())
questions = []
for i in range(D):
    p , c = map(int,input().split())
    tmp = []
    for j in range(p):
        if j == p - 1:
            tmp.extend([c])
        else:
            tmp.extend([(i + 1) * 100])
    questions.append(tmp)
questions = [for x in zip(*questions)]
print(questions)
ans = 0


print(solve(0,0))