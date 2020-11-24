def cnt_Leap_year(x):
    return x // 4 - x // 100 + x // 400
A, B = map(int, input().split())
A_cnt = cnt_Leap_year(A - 1)
B_cnt = cnt_Leap_year(B)
print(B_cnt - A_cnt)