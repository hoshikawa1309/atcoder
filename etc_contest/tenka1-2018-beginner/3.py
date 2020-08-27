from collections import deque
N = int(input())
A = list(int(input()) for _ in range(N))
A.sort()
ans1 = deque()
ans2 = deque()
if N % 2 == 1:
    A_before = deque(A[:N // 2 + 1])
    A_after = deque(A[N // 2 + 1:])
else:
    A_before = deque(A[:N // 2])
    A_after = deque(A[N // 2:])
print(A_before)
print(A_after)
for i in range(len(A_after)):
    if i % 2 == 0:
        ans1.append(A_before.pop())
        ans1.append(A_after.pop())
    else:
        ans2.append(A_before.pop())
        ans2.append(A_after.pop())
if A_before:
    ans1.append(A_before.pop())
while ans2:
    tmp = ans2.pop()
    ans1.append(tmp)
ans = 0
print(ans1)
for i in range(len(ans1) - 1):
    ans += abs(ans1[i] - ans1[i + 1])
print(ans)

