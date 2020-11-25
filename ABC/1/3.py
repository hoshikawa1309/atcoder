from decimal import Decimal, ROUND_HALF_UP
directions = ['NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW',  'WSW',  'W', 'WNW', 'NW', 'NNW','N']
lower_power = [0, 3, 16, 34, 55, 80, 108, 139, 172, 208, 245, 285, 327]
Deg, dis = map(int, input().split())
idx = (10 * Deg + 1125) // 2250 - 1
x = dis / 6 + 0.000000001
x = Decimal(str(x)).quantize(Decimal('1'), ROUND_HALF_UP)
ans_power = 0
for i in range(len(lower_power)):
    if lower_power[i] <= x:
        ans_power = i
direction = directions[idx]
if ans_power == 0:
    direction = 'C'
print(direction, ans_power)
