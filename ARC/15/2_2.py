N = int(input())
cnt_list = [0] * 6
for _ in range(N):
    Mt, mt = map(float, input().split())
    if 35 <= Mt:
        cnt_list[0] += 1
    if 30 <= Mt < 35:
        cnt_list[1] += 1
    if 25 <= Mt < 30:
        cnt_list[2] += 1
    if 25 <= mt:
        cnt_list[3] += 1
    if mt < 0 and 0 <= Mt:
        cnt_list[4] += 1
    if Mt < 0:
        cnt_list[5] += 1
print(*cnt_list)