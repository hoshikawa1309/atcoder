from collections import deque
s = deque(input())
ans = 0
while len(s) > 1:
    if s[0] == s[-1]:
        s.popleft()
        s.pop()
    elif s[0] == 'x':
        ans += 1
        s.popleft()
    elif s[-1] == 'x':
        ans += 1
        s.pop()
    else:
        print(-1)
        exit()
print(ans)
