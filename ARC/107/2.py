def f(x):
    # (a + b == x)となる(a, b)の個数
    return max(min((2 * N - x + 1), x - 1), 0)


N, K = map(int, input().split())
# K = -K if K < 0 else K
ans = 0
for i in range(2, 2 * N + 1):
    # 上限も決めよう
    if i - K >= 2:
        print(i)
        print('f(i) : ', f(i))
        print('f(i - K) : ', f(i - K))
        ans += f(i) * f(i - K)
print(ans)