N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
positive = []
negative = []
for a, b in zip(A,B):
    now = a - b
    if now > 0:
        positive.append(now)
    elif now < 0:
        negative.append(-now)
if not negative:
    print(0)
    exit()
if sum(positive) < sum(negative):
    print(-1)
    exit()
positive.sort(reverse=True)
n_sum = sum(negative)
ans = 0
for p in positive:
    ans += 1
    n_sum -= p
    if n_sum <= 0:
        break
print(ans + len(negative))


