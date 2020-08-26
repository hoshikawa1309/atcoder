N = int(input())
edges = []
for _ in range(N):
    edge = int(input())
    edges.append(edge)
print(sum(edges))
is_triangle = False
ans = float('inf')
a = 0
for i in range(N - 1):
    a += edges[i]
    b = 0
    c = sum(edges[i + 1:])
    for j in range(i + 1, N):
        b += edges[j]
        c -= edges[j]
        if a + b > c and b + c > a and c + a > b:
            is_triangle = True
            break
        ans = min(ans, abs(b - a - c))
if is_triangle:
    print(0)
else:
    a = sum(edges)
    b = 0
    for i in range(N):
        a -= edges[i]
        b += edges[i]
        ans = min(ans, abs(a - b))
    print(ans)