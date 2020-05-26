N, K = map(int, input().split())
num = [0] * K
# numにmod K の個数を入れる
for i in range(1, N + 1):
    num[i % K] += 1
ans = 0
# print(num)


for a in range(K):
    # (a + b) mod K == 0 and(a + c) mod K == 0となるbとcのmodを求める
    b = c = (K - a) % K
    # print(a, b, c)
    if (b + c) % K != 0:
        continue
    # a ,b ,c の順列を加算する
    ans += num[a] * num[b] * num[c]
print(ans)