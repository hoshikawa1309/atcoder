def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

N, X = map(int, input().split())
x = list(map(int, input().split()))

x.insert(0, X)
distance = []
for i in range(1, len(x)):
    distance.append(abs(x[i] - x[i - 1]))


ans = distance[0]
for i in range(1, len(distance)):
    ans = gcd(distance[i], ans)
print(ans)