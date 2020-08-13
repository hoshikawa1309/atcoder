N = int(input())
num = [0] * (10 ** 6 + 1)
for _ in range(N):
    score = int(input())
    num[score] += 1
cumulative_sum = [0] * (10 ** 6 + 1)
cumulative_sum[10 ** 6] = num[10 ** 6]
for i in range(10 ** 6 - 1, -1, -1):
    cumulative_sum[i] = num[i] + cumulative_sum[i + 1]
print(num[:11])
print(cumulative_sum[:11])
flag = True
for i in range(1, 10 ** 6 + 1):
    if num[i] > 0:
        flag = False
        break

def bisect_left_reverse(a, x):
    '''
    reverseにソートされたlist aに対してxを挿入できるidxを返す。
    xが存在する場合には一番左側のidxとなる。
    '''
    if a[0] <= x:
        return 0
    if x < a[-1]:
        return len(a)
    # 二分探索
    ok = len(a) - 1
    ng = 0
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if a[mid] <= x:
            ok = mid
        else:
            ng = mid
    return ok

Q = int(input())
if flag:
    for _ in range(Q):
        k = int(input())
        print('0')
    exit()
for _ in range(Q):
    k = int(input())
    idx = bisect_left_reverse(cumulative_sum, k)
    if cumulative_sum[idx] == k and cumulative_sum[idx] != 0:
        print(max(idx - 1, 0))
    else:
        print(idx)