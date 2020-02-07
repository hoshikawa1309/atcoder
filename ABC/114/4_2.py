N = int(input())
num_list = [3, 5, 7]


def Base_10_to_n(X, n):
    if (int(X / n)):
        return Base_10_to_n(int(X / n), n) + str(X % n)
    return str(X % n)

ans = 0
i = 5
while True:
    tmp = Base_10_to_n(i, 3)
    base = 1
    num10 = 0
    tmp = list(tmp)
    if len(tmp) < 3:
        tmp.insert(0, "0")

    for j in range(len(tmp) - 1, -1, -1):
        idx = int(tmp[j])
        num10 += num_list[idx] * base
        base *= 10
    if num10 > N:
        break
    # print(tmp)


    tmp = set(tmp)
    if {'0', '1', '2'} == tmp:
        ans += 1
    i += 1
print(ans)