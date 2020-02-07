import math
N, D, A = map(int, input().split())
monstars = [list(map(int, input().split())) for _ in range(N)]
monstars.sort()

field = [0] * (2 * 10 ** 5 + 1)
first_damage = math.ceil(monstars[0][1] / A)
field[monstars[0][0]] = first_damage
field[monstars[0][0] + 2 * D + 1] = -first_damage

now = 0
enemy_idx = 0
ans = first_damage
for i in range(2 * 10 ** 5):
    now += field[i]
    if monstars[enemy_idx][0] == i:
        if now * A < monstars[enemy_idx][1]:
            add_boms = math.ceil((monstars[enemy_idx][1] - (now * A)) / A)
            field[i] += add_boms
            end = min(monstars[enemy_idx][0] + 2 * D + 1, 2 * 10 ** 5 + 1)
            field[monstars[enemy_idx][0] + 2 * D + 1] = -add_boms
            ans += add_boms
            now += add_boms
        enemy_idx = min(enemy_idx + 1, N - 1)

print(ans)