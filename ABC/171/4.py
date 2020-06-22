from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
Counter = defaultdict(int)
for a in A:
    Counter[a] += 1
sum_val = sum(A)
ans = []
for _ in range(Q):
    B, C = map(int, input().split())
    sum_val += (C - B) * Counter[B]
    Counter[C] += Counter[B]
    Counter[B] = 0
    ans.append(sum_val)
print(*ans, sep='\n')
