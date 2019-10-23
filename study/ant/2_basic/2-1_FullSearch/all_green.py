D , G = map(int,input().split())
questions = []
for i in range(D):
    p , c = map(int,input().split())
    questions.append([p,c])

ans = float("inf")
for bit in range(2 ** D):
    tmp_ans = 0
    tmp_sum = 0
    for j in range(D):
        if bit >> j & 1:
            tmp_sum += questions[j][0] * 100 * (j + 1) + questions[j][1]
            tmp_ans += questions[j][0]
    if tmp_sum < G:
        for j in range(D - 1 , -1 , -1):
            if bit >> j & 1:
                continue
            else:
                for k in range(questions[j][0]):
                    tmp_ans += 1
                    tmp_sum += 100 * (j + 1)
                    if tmp_sum >= G:
                        break
                if tmp_sum >= G:
                    break
    if tmp_ans < ans and tmp_sum >= G:
        ans = tmp_ans
print(ans)