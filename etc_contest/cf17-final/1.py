from collections import deque
S = deque(input())
if len(S) < 5 or 9 < len(S):
    print('NO')
    exit()
flag = True
while flag:
    for i in range(len(S) - 1):
        if S[i] == S[i + 1] == 'A':
            a1 = S.popleft()
            a1 = S.popleft()
            S.appendleft(a1)
            break
    else:
        flag = False

ans = []
for i in range(9):
    if i % 2 == 0 and i != 2:
        ans.append('A')
    elif not S:
        break
    else:
        tmp = S.popleft()
        while tmp == 'A' and S:
            tmp = S.popleft()
        ans.append(tmp)
if ''.join(ans) == 'AKIHABARA':
    print('YES')
else:
    print('NO')