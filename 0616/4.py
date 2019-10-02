N , K = map(int ,input().split())
A = list(map(int , input().split()))
cnt = 0
''' 単純に全探索。確実にTLE
for i in range(N):
    for j in range(i + 1 , N + 1):
        if sum(A[i:j]) >= K:
            cnt += 1
'''
right = 0
s = 0
for left in range(N):
    # for j in range(i + 1,N + 1):
    while right < N and s < K:
        s += A[right]
        right += 1
    if s < K:
        break
    else:
        cnt += N - right + 1
        s -= A[left]
print(cnt)