N, T = map(int, input().split())
t = list(map(int, input().split()))
end_time = T + t[0]
sum_time = T
for i in range(1, N):
    sum_time += T - max(0, end_time - t[i])
    end_time = T + t[i]
print(sum_time)