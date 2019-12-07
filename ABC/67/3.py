N = int(input())
A = list(map(int,input().split()))
A = A[::-1]
x = sum(A) - A[0]
y = A[0]
ans = abs(x - y)
for i in range(1,N - 1):
    y += A[i]
    x -= A[i]
    tmp_ans = abs(x - y)
    if tmp_ans < ans:
        ans = tmp_ans
print(ans)
