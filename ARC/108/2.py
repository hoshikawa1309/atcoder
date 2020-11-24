from collections import deque
N = int(input())
s = deque(input())
t = deque()
while s:
    t.append(s.popleft())
    if len(t) < 3:
        continue
    if t[-3] == 'f' and t[-2] == 'o' and t[-1] == 'x':
        for _ in range(3):
            t.pop()
print(len(t))