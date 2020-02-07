def rec(n):
    if n == 0:
        return 1
    return rec(n - 1) * 2 + 3

N = int(input())
print(rec(N))