N = int(input())
AB = list(list(map(int, input().split())) for _ in range(N))
AB.sort(key=lambda x: x[1])
now = 0
for a, b in AB:
    now += a
    if now > b:
        print("No")
        exit()
print("Yes")