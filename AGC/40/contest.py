N = int(input())
questions = [list(map(int,input().split())) for _ in range(N)]
questions.sort()
#print(questions)
ans = 0
for i in range(N - 1):
    if i == 0:
        left, right = questions[0][0] , questions[0][1]
        s1 = right - left + 1
        left, right = max(questions[i + 1][0], questions[N - 1][0]), min(questions[i + 1][1], questions[N - 1][1])
        s2 = right - left + 1
    elif i == N - 2:
        left, right = max(questions[0][0], questions[i][0]), min(questions[0][1], questions[i][1])
        s1 = right - left + 1
        left, right = questions[N - 1][0], questions[N - 1][1]
        s2 = right - left + 1
    else:
        left , right = max(questions[0][0] , questions[i][0]) , min(questions[0][1] , questions[i][1])
        s1 = right - left + 1
        left , right = max(questions[i + 1][0] , questions[N - 1][0]) , min(questions[i + 1][1] , questions[N - 1][1])
        s2 = right - left + 1

    tmp_ans = s1 + s2
    print(tmp_ans)
    if tmp_ans > ans:
        ans = tmp_ans
print(ans)