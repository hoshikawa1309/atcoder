N = int(input())
A = list(map(int, input().split()))
A.sort()
flags = [False] * 8
min_ans = 1
high_coder = 0
for i in range(N):
    idx = A[i] // 400
    if idx < 8:
        flags[idx] = True
        min_ans = sum(flags)
    else:
        high_coder = N - i
        break

print(min_ans, sum(flags) + high_coder)

