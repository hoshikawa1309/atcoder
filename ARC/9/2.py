b = list(map(int, input().split()))
N = int(input())
A = []
outputs = []
d = {}
for _ in range(N):
    a = int(input())
    A.append(a)
for a in A:
    tmp = a
    output = ''
    while a:
        output += str(b.index(a % 10))
        a //= 10
    outputs.append(int(output[::-1]))
    d[output[::-1]] = int(tmp)
outputs.sort()
# print(outputs)
for output in outputs:
    print(d[str(output)])