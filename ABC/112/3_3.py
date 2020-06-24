N = int(input())
pyramid_height = []
for _ in range(N):
    val = list(map(int, input().split()))
    pyramid_height.append(val)

pyramid_height.sort(key=lambda x: x[2], reverse=True)

for x in range(101):
    for y in range(101):
        tmp_h = pyramid_height[0][2] + abs(x - pyramid_height[0][0]) + abs(y - pyramid_height[0][1])
        for i in range(1, N):
            if pyramid_height[i][2] != max(tmp_h - abs(x - pyramid_height[i][0]) - abs(y - pyramid_height[i][1]), 0):
                break
        else:
            print(x, y, tmp_h)
            exit()


