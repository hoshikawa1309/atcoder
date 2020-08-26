def solve(x, y, W):
    def direction1(now_x, now_y, now_w):
        if W == 'R':
            if now_x == 8:
                now_x -= 1
                now_w = 'L'
            else:
                now_x += 1
        elif W == 'L':
            if now_x == 0:
                now_x += 1
                now_w = 'R'
            else:
                now_x -= 1
        elif W == 'U':
            if now_y == 0:
                now_y += 1
                now_w = 'D'
            else:
                now_y -= 1
        elif W == 'D':
            if now_y == 8:
                now_y -= 1
                now_w = 'U'
            else:
                now_y += 1
        return now_x, now_y, now_w

    def direction2(now_x, now_y, now_w):
        if now_w == 'RD':
            if now_x == 8 and now_y == 8:
                now_x -= 1
                now_y -= 1
                now_w = 'LU'
            elif now_x == 8:
                now_x -= 1
                now_y += 1
                now_w = 'LD'
            elif now_y == 8:
                now_x += 1
                now_y -= 1
                now_w = 'RU'
            else:
                now_x += 1
                now_y += 1
        elif now_w == 'RU':
            if now_x == 8 and now_y == 0:
                now_x -= 1
                now_y += 1
                now_w = 'LD'
            elif now_x == 8:
                now_x -= 1
                now_y -= 1
                now_w = 'LU'
            elif now_y == 0:
                now_x += 1
                now_y += 1
                now_w = 'RD'
            else:
                now_x += 1
                now_y -= 1
        elif now_w == 'LU':
            if now_x == 0 and now_y == 0:
                now_x += 1
                now_y += 1
                now_w = 'RD'
            elif now_x == 0:
                now_x += 1
                now_y -= 1
                now_w = 'RU'
            elif now_y == 0:
                now_x -= 1
                now_y += 1
                now_w = 'LD'
            else:
                now_x -= 1
                now_y -= 1
        elif now_w == 'LD':
            if now_x == 0 and now_y == 8:
                now_x += 1
                now_y -= 1
                now_w = 'RU'
            elif now_x == 0:
                now_x += 1
                now_y += 1
                now_w = 'RD'
            elif now_y == 8:
                now_x -= 1
                now_y -= 1
                now_w = 'LU'
            else:
                now_x -= 1
                now_y += 1
        return now_x, now_y, now_w
    ans = [c[y][x]]
    for _ in range(3):
        if len(W) == 1:
            x, y, W = direction1(x, y, W)
        else:
            x, y, W = direction2(x, y, W)
        # print(x, y, W)
        ans.append(c[y][x])
    print(*ans, sep='')

if __name__ == '__main__':
    x, y, W = input().split()
    x, y = int(x) - 1, int(y) - 1
    c = []
    for _ in range(9):
        s = list(input())
        c.append(s)
    solve(x, y, W)

    '''
    # ---test---
    dir = ['U', 'R', 'D', 'L']
    xx = [0]
    yy = [0]
    for x in xx:
        for y in yy:
            for w in dir:
                print('(x, y, w) = ({}, {}, {})'.format(x, y, w))
                solve(x, y, w)
    '''