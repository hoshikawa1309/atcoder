N = int(input())
# N = 4
stones = list(input())
# stones = ['W','R','R','R']
if not ('R' in stones and 'W' in stones):
    print('0')
    exit()
right = 0
left = N - 1
white_idx = -1
red_idx = -1
ans = 0
while right < left:
    while right < N and right < left:
        if stones[right] == 'W':
            white_idx = right
            break
        right += 1
    while 0 < left and right < left:
        if stones[left] == 'R':
            red_idx = left
            break
        left -= 1
    if left == right:
        break
    if 0 <= white_idx and 0 <= red_idx:
        ans += 1
    right += 1
    left -= 1
print(ans)