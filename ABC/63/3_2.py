N = int(input())
scores = list(int(input()) for _ in range(N))
ans = sum(scores)
if ans % 10 != 0:
    print(ans)
    exit()

scores.sort()
for score in scores:
    if score % 10 != 0:
        ans -= score
        print(ans)
        exit()
print('0')
