def move(command, x, y):
    if command == 'U':
        y += 1
    elif command == 'D':
        y -= 1
    elif command == 'L':
        x -= 1
    else:
        x += 1
    return [x, y]


S = input()
T = int(input())
now = [0, 0]
hatena_cnt = 0
for i in range(len(S)):
    if S[i] == '?':
        hatena_cnt += 1
    else:
        now = move(S[i], now[0], now[1])
distance = abs(now[0]) + abs(now[1])
if T == 1:
    print(distance + hatena_cnt)
else:
    if distance >= hatena_cnt:
        print(distance - hatena_cnt)
    else:
        tmp = hatena_cnt - distance
        print(tmp % 2)