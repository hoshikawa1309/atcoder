directions = ['NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW',  'WSW',  'W', 'WNW', 'NW','NNW','N']
Deg, dis = map(int, input().split())
Deg = int((10 * Deg) + 0.00001)
if Deg < 1125 or 34875 <= Deg:
    Deg = 0
else:
    Deg = (Deg - 1125) // 2250
if dis == 0:
    dir = 'C'
else:
    dir = directions[Deg]
print(dir)