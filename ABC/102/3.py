# abs(Ai - (b - i )) + ... のmin
N = int(input())
A = list(map(int,input().split()))
sum = 0
for i in range(len(A)):
    sum += A[i] - (i + 1)
print(sum)
print(sum // N)