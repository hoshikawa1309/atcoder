N , M = map(int,input().split())
drink = []
for _ in range(N):
    a , b = map(int,input().split())
    drink.append([a,b])
drink.sort()


value = 0
hold = 0
while hold != M:
    if drink[0][1] == 0:
        drink.pop(0)
    value += drink[0][0]
    hold += 1
    drink[0][1] -= 1
print(value)