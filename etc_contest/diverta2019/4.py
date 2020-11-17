N = int(input())
ans = 0
for r in range(1, N):
    if r ** 2 > N:
        break
    # mが整数値にならない。または、商とあまりの関係を示さないときcontinue
    if (N - r) % r != 0 or (N - r) // r <= r:
        continue
    m = (N - r) // r
    ans += m
print(ans)