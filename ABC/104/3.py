D , G = map(int,input().split())
bonus = []
question_cnt = []
for i in range(D):
    p , c = map(int,input().split())
    question_cnt.append(p)
    bonus.append(c)
ans = float('inf')
for bit in range(2 ** D):
    sum_val = 0
    tmp_ans = 0
    Flag = False
    for j in range(D):
        if bit >> j & 1:
            sum_val += question_cnt[j] * (j + 1) * 100 + bonus[j]
            tmp_ans += question_cnt[j]
    if sum_val < G:
        for j in range(D-1 , - 1 , -1):
            if Flag:
                break
            if not bit >> j & 1:
                Flag = True
                for k in range(question_cnt[j]):
                    sum_val += (j + 1) * 100
                    tmp_ans += 1
                    if sum_val >= G:
                        break
    if tmp_ans < ans and sum_val >= G:
        ans = tmp_ans
print(ans)



