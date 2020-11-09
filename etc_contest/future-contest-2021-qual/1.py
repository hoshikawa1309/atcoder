from collections import deque
cards = [list(map(int, input().split())) for _ in range(100)]
# print(cards)
'''
def bfs(now_x, now_y, target_card):
    q = deque()
    q.append([now_x, now_y])
    target_x = cards[target_card][0]
    target_y = cards[target_card][1]
    while q:
        for dx, dy in zip(dx_list, dy_list):
            next_x, next_y = now_x + dx, now_y + dy
            if next_x < 0 or 20 <= next_x or next_y < 0 or 20 <= next_y:
                continue
            if next_y == target_y and next_x == target_x:
                return target_x,
'''

move = ''
x = 0
y = 0
dx_list = [0, 1, 0, -1]
dy_list = [1, 0, -1, 0]
for next_x, next_y in cards:
    if x < next_x:
        move += 'D' * (next_x - x)
    elif next_x < x:
        move += 'U' * (x - next_x)
    if y < next_y:
        move += 'R' * (next_y - y)
    elif next_y < y:
        move += 'L' * (y - next_y)
    move += 'I'
    x, y = next_x, next_y
print(move)
print('DDDDDDDDDDDDDDDRRRRRRRRRRRRRRRRRRRIUUUUUUULLLLLLLLLLLLLLLLLLIUUUUURRRRRRRRRRRRIURRRRRRIDDDDDDDDDDDDDDDLLLLLLLLLIUUULLLLLLLIUUUUUUUUUUULIDDDDDDDDDDDDDDDDRRIUUUUUUUUUUUUULLIDDDDDDDDDDDDLIUUUUUUUUUUUUUURRRIURRRRRRIUUURRRRRIDDLLLLLLLLLLIDDDDDDDDRRIUUUULLLLIDDDDDDDDDDDDDRRRRRRRRRIUUUUUUUUUUUUUUUUUULLLLLLLLLLLLIDDDDDDDDDDDDDDDDDDRRRIUUUUUUUUUUUUUUULLIUUUURRRRRIDDDDDDDDDDRRRRRRRRRRRRIDDLLLLLLIUUUURIUULLLLLLLLLIDDDDLLIUUUURRRRRRRRRRIUUUULLLLLLLLLLLLIUURRRRRRRRRRRIDDDDDDLLIDDLLLLLLIDDDDDRRRRRRIUUUULLLLLLLLLIDDRRRRRRRRRRRRRRRRRIUULLLLLLLLLLLLLIDDDLLLIUUUUUUUUUUURRRRRRRRRRRRRRRRRIDDDDDDDDDDDDDDDDDDRIUUUUUUUUUULLLLLLLLLLIUUUUUUURRIDDDDDDRRRRRRRRIDDDDDDDDDDLLLLLLLLLLLLLLLLIUUUUUUUUUUUUUUUURRRRRRRRRRRRIDDDDDDRIDDDDDDDDLLLLLLLLLLLLLLIUUUUUUUUUUUURRRIDDDDDDDDDDLIUUUUULIDDDDDDRRRRRRRRRRIUUUUUUUUUUUULLLLLLLLLLLLLIDDDDDRRRRRRRRRRRIDDDDDDDLLLLLLLIUUUUUUUUUUUUUUURRRIDDDDDDDDDDDDRRRRRRRRRRRRIDDDDDDLLLLLLLLLLLLIUUUUUURRRRRRRRRRIUUUULLLLLLLLLLLLLLLIUULLIUUUUURRRRRRRIDDDDDDDDDDDDDDDDLLLLLLLIURRRRRRRRRRIUUUUUUUUUUUUUUULLLLIDDDDDDDDDLIUUUUUURRRRRRRRRIDDDDDDDDLLLLLLLIUUUUUURRRRILLLLLIDDDDDDDDRRRRRRRRRRRRRIDLLLLIDDRIUUUUUUUUUUUUUUUULLLLIDDDDDDLLLIUUUUULLIDDIUUULLLIDDDDLIUUUUURRRRRRRRRRRRRRIDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLIUUUUUUUUUUUURRRRRRRRRRIDDDDRRRIDDDLLLIULIDDDDRRRRRRIUUUUUUUUUUUUUUULLLLLLLLIDDDDDDDDDDDDDDDDDDDLLLLIUUUUUUULLIUURRRRIDDDDDLLLLLLLIUUUUURRRRRRRRRRRRIDDDDDDDRRIUUUUUUUUUUUUUUUULLLLLLLLLLIDDDDDDDDDDDDDDRRRRRRRRRIDDDDLLLLLLLLLIUURRIUUUUUUUUUUUUUUURRRRRRRRRRRIDDDLLLLLLLLLLLIDDDDDDDLIUUUUUUUUUIDDDDDDDDDDDDDDDDRIUUUUUUUUUUUUUUUUUURRRRRRRRRI')