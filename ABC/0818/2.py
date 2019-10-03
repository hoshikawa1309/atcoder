N = int(input())
A = [ i for i in map(int , input().split())]
den_sum = 0
for j in range(len(A)):
    den_sum += 1 / A[j]

print(1 / den_sum)
