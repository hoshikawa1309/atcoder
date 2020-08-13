N, A, B = map(int, input().split())
if (B - A) % 2 == 0:
    print((B - A) // 2)
else:
    # N に向かうことを考える
    A_to_N_dis = N - B + 1
    A_to_N = A + A_to_N_dis
    tmp_ans = (N - A_to_N) // 2 + A_to_N_dis

    # 1に向かうことを考える
    B_to_1_dis = A - 1 + 1
    B_to_1 = B - B_to_1_dis
    ans = (B_to_1 - 1) // 2 + B_to_1_dis
    print(min(tmp_ans, ans))