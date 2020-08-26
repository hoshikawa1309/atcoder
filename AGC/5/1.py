from collections import deque
right = deque(input())
left = deque()
while right:
    left.append(right.popleft())
    if not right:
        break
    while left and right and left[-1] == 'S' and right[0] == 'T':
        left.pop()
        right.popleft()
print(len(left))