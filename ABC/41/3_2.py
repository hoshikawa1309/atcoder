N = int(input())
A = list(map(int, input().split()))
tmp = []
for i, v in enumerate(A):
    tmp.append([v, i])
tmp.sort(reverse=True)
for v, i in tmp:
    print(i + 1)