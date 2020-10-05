N, X, M = map(int,input().split())
exist = set([X])
order = [X]
now = X
while True:
    next_val = now ** 2 % M
    if next_val in exist:
        break
    order.append(next_val)
    exist.add(next_val)
    now = next_val
# print(order)
flag = False
loop = []
for i in range(len(order)):
    if order[i] == next_val:
        flag = True
    if flag:
        loop.append(order[i])
if N <= len(order):
    ans = sum(order[:N])
else:
    ans = sum(order)
    N -= len(order)
    ans += sum(loop) * (N // len(loop))
    ans += sum(loop[:N % len(loop)])
print(ans)