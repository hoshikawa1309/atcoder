N, T = map(int, input().split())
Time = list(map(int, input().split()))
end = T
ans = T
for i in range(1, N):
    start = Time[i]
    duplication = max(end - start, 0)
    ans += T - duplication
    end = start + T
print(ans)
