N, M = map(int, input().split())
X = list(map(int, input().split()))
W = list(map(int, input().split()))
X.sort()

left = [0] * (N + 1)
right = [0] * (N + 1)
for i in range(2, N, 2):
    left[i] = left[i - 2] + X[i - 1] - X[i - 2]
    right[i] = right[i - 2] + X[N - i + 1] - X[N - i]
print(left)
print(right)
