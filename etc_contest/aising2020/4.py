def f(n, c_one):
    cnt = 0
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
binary_str = str(input())
# N = 2 * 10 ** 5
# binary_str = '1' * (2 * 10 ** 5)
binary_num = int(binary_str, 2)
cnt_one = binary_str.count('1')
for i in range(N):
    idx = (N - 1 - i)
    if binary_str[i] == '1':
        print(f(binary_num - 2 ** idx, cnt_one - 1))
    else:
        print(f(binary_num + 2 ** idx, cnt_one + 1))
