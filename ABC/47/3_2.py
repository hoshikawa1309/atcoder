S = input()
now = S[0]
ans = 0
for stone in S:
    if stone != now:
        now = stone
        ans += 1
print(ans)