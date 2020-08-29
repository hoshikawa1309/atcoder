N, A, B = map(int, input().split())
min_val = A * (N - 1) + B
max_val = A + B * (N - 1)
print(max(0, max_val - min_val + 1))