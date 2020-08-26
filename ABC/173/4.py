N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
if N == 2:
    print(A[0])
    exit()
ans = 0
second_half = N // 2
first_half = N - second_half
for i in range(first_half - 1):
    ans += A[i]
if N % 2 == 1:
    for i in range(second_half):
        ans += A[i + 1]
else:
    for i in range(second_half - 1):
        ans += A[i + 1]
    ans += A[second_half - 1]
print(ans)