S = int(input()) + 1
for x in range(1, int(S ** 0.5) + 1):
    if S % x == 0:
        if x != S // x:
            y = S // x
        if x <= 10 ** 9 and y <= 10 ** 9:
            break
print(1, y, x, 1, 0 ,0)

