N , K = map(int,input().split())
A = list(map(int,input().split()))
max = 0


for i in range(K + 1):
    sum = 0
    for j in range(N):
        sum += A[j] ^ i
        if sum > max:
            max = sum
print(max)