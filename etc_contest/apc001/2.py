N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
step = sum(B) - sum(A)
if step < 0:
    print('No')
    exit()

a_cnt = 0
b_cnt = 0

for a, b in zip(A, B):
    tmp = a - b
    if tmp > 0:
        b_cnt += tmp
    elif tmp < 0:
        tmp = abs(tmp)
        if tmp % 2 == 0:
            a_cnt += tmp // 2
        else:
            a_cnt += tmp // 2 + 1
            b_cnt += 1
if step >= a_cnt >= b_cnt:
    print('Yes')
else:
    print('No')
