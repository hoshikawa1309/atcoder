def f(n, c_one):
    cnt = 1
    while n:
        n = n % c_one
        cnt += 1
        # c_one = bin(n).count('1') # ここがボトルネック
        c_one = 0
        tmp = n
        while tmp:
            if tmp % 2 == 1:
                c_one += 1
            tmp //= 2
    return cnt


N = int(input())
X = input()
X_one_cnt = X.count('1')
X_num = int(X, 2)
X_mod_one = X_num % (X_one_cnt + 1)
X_mod_zero = X_num % (X_one_cnt - 1)
for i in range(N):
    calculate_num = 2 ** (N - i - 1)
    if X[i] == '0':
        if X_num + calculate_num == 0:
            print('0')
        else:
            step_after = (X_mod_one + calculate_num) % (X_one_cnt + 1)
            print(f(step_after, bin(step_after).count('1')))
    else:
        if X_num - calculate_num == 0:
            print('0')
        else:
            step_after = (X_mod_zero - calculate_num) % (X_one_cnt - 1)
            print(f(step_after, bin(step_after).count('1')))