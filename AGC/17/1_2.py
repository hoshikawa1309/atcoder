from math import factorial
N, P = map(int, input().split())
A = list(map(int, input().split()))
A = list(map(lambda x: x % 2, A))
counter = {'0': 0, '1': 0}
for a in A:
    c_a = str(a)
    counter[c_a] += 1
#print(counter)
ans = 2 ** counter['0']
tmp = factorial(counter['1'])
tmp_ans = 0
for i in range(0 + P,counter['1'] + 1,2):
    tmp_ans += tmp / factorial(i) / factorial(counter['1'] - i)
print(int(tmp_ans * ans))
