N , M = map(int,input().split())
lst = []
AC_list = [False] * N
WA_cnt_list = [0] * N
for _ in range(M):
    r , judge = input().split()
    question_num = int(r) - 1
    if AC_list[question_num]:
        continue
    elif judge == "WA":
        WA_cnt_list[question_num] += 1
    elif judge == "AC":
        AC_list[question_num] = True
wa_cnt = 0
for i in range(N):
    if AC_list[i]:
        wa_cnt += WA_cnt_list[i]
print(sum(AC_list) , wa_cnt)
