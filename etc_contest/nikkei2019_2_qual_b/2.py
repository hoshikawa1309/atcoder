from collections import Counter
mod = 998244353
N = int(input())
D = list(map(int, input().split()))
if D[0] != 0:
    print('0')
    exit()
counter = Counter(D)
if counter[0] != 1:
    print('0')
    exit()
counter = sorted(counter.items())
# print(counter)
keys = []
values = []
for i in range(len(counter)):
    keys.append(counter[i][0])
    values.append(counter[i][1])
for i in range(len(keys)):
    if i != keys[i]:
        print('0')
        exit()
ans = 1
for i in range(1, len(counter) - 1):
    ans *= pow(values[i], values[i + 1], mod)
    ans %= mod
print(ans)