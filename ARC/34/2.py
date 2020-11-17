def f(x):
    str_i = str(x)
    tuple_i = tuple(map(int, str_i))
    return sum(tuple_i)


N = int(input())
ans = []
for x in range(max(0, N - 200), N + 1):
    if x + f(x) == N:
        ans.append(x)
print(len(ans))
if len(ans):
    print(*ans, sep='\n')
