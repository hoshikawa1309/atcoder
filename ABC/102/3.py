# abs(Ai - (b - i )) + ... のmin
N = int(input())
A = list(map(int,input().split()))
B = []
for i in range(len(A)):
    B.append(A[i] - (i + 1))
B.sort()
#print(B)
if N % 2 == 1:
    b = B[N//2]
else:
    b = (B[N // 2] + B[N // 2 - 1]) // 2
#print(b)
sum_val = 0
for i in range(N):
    sum_val += abs(B[i] - b)
print(sum_val)