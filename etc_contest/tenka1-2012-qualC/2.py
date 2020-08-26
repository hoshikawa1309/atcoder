from collections import deque
s = deque(input())
goals = ['S10', 'SJ', 'SQ', 'SK', 'SA', 'H10', 'HJ', 'HQ', 'HK', 'HA', 'D10', 'DJ', 'DQ', 'DK', 'DA', 'C10', 'CJ', 'CQ','CK', 'CA']
goals_flags = [False] * 20
ans = []
target = ''
while s:
    mark = s.popleft()
    if s[0] == '1' and s[1] == '0':
        num = '10'
        for _ in range(2):
            s.popleft()
    else:
        num = s.popleft()
    now = mark + num
    if now in goals:
        goals_flags[goals.index(now)] = True
        if all(goals_flags[:5]):
            # print('S')
            target = 'S'
            break
        elif all(goals_flags[5:10]):
            # print('H')
            target = 'H'
            break
        elif all(goals_flags[10:15]):
            # print('D')
            target = 'D'
            break
        elif all(goals_flags[15:]):
            # print('C')
            target = 'C'
            break
    ans.append(now)

nums = ['10', 'J', 'Q', 'K', 'A']

if len(ans) == 4:
    print(0)
else:
    for i in range(len(ans)):
        for num in nums:
            if ans[i] == target + num:
                break
        else:
            print(ans[i], end='')
    print()
