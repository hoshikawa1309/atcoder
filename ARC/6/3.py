N = int(input())
positions = []
ans = 0
for _ in range(N):
    w = int(input())
    stack_box = -1
    for i in range(len(positions)):
        if w <= positions[i] and positions[stack_box] >= positions[i]:
            stack_box = i
    if stack_box >= 0:
        positions[stack_box] = w
    else:
        positions.append(w)
print(len(positions))
