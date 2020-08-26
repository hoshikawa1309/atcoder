from collections import deque
K = int(input())
q = deque([i for i in range(1, 10)])
for _ in range(K - 1):
    # 13print(q)
    num = q.popleft()
    for i in range(-1,2):
        if 0 <= int(str(num)[-1]) + i <= 9:
            q.append(num * 10 + int(str(num)[-1]) + i)
# print(len(q))
print(q[0])
