N , K = map(int ,input().split())
S = list(input())

a = []

now = S[0]
cnt = 1
for x in S[1:]:
    if x == now:
        cnt += 1
    else:
        a.append(cnt)
        now = x
        cnt = 1
a.append(cnt)

#偶数番目に0の数、奇数番目に1の数
if S[0] == "0":
    a = [0] + a
if S[-1] == "0":
    a = a + [0]

#print(a)

m = len(a)

if 2 * K + 1 >= m:
    maxsum = N
else:
    l = 0
    r = 2 * K + 1
    nowsum = sum(a[l : r])
    maxsum = nowsum
    while True:
        l += 2
        r += 2
        if r > m:
            break
        nowsum += a[r - 2] + a[r - 1] - (a[l - 2] + a[l - 1])
        maxsum = max(maxsum , nowsum)

print(maxsum)

'''バグるしTLE
N , K = map(int ,input().split())
S = list(input())
if not '0' in S:
    print(N)
    exit()

target_char = S[0]
max_val = 0
cnt = 1
zero_list = []
one_list = []
for i in range(1,N):
    if S[i] == target_char:
        cnt += 1

    else:
        if target_char == "0":
            zero_list.append(cnt)
            cnt = 1
            target_char = "1"
        else:
            one_list.append(cnt)
            cnt = 1
            target_char = "0"
    if i == N - 1:
        if target_char == '0':
            zero_list.append(cnt)
        else:
            one_list.append(cnt)
#print(one_list)
#print(zero_list)
i = 0
max_val = 0

if S[0] == "1":
    first_one = one_list[0]
    one_list.pop(0)

for i in range(len(zero_list) - K + 1):
    sum_val = 0

    if S[0] == "1" and i == 0:
        sum_val += first_one
    if S[0] == "0" and i == 0:
        sum_val += sum(zero_list[i:i + K]) + sum(one_list[i:i + K ])
    else:
        if i == 0:
            sum_val += sum(zero_list[i:i + K]) + sum(one_list[i:i + K])
        else:
            sum_val += sum(zero_list[i:i+K]) + sum(one_list[i - 1:i + K + 1])
    if max_val < sum_val:
        max_val = sum_val
print(max_val)
'''