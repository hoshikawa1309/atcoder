N = int(input())
music = [list(input().split()) for _ in range(N)]
X = input()
X_after = False
ans = 0
for i in range(N):
    if X_after:
        ans += int(music[i][1])
    elif X == music[i][0]:
        X_after = True
print(ans)