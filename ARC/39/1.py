A, B = input().split()
A = list(A)
B = list(B)
max_val = int(''.join(A)) - int(''.join(B))
for i in range(3):
    tmp = A[i]
    A[i] = '9'
    max_val = max(int(''.join(A)) - int(''.join(B)), max_val)
    A[i] = tmp

for i in range(3):
    tmp = B[i]
    if i == 0 :
        B[i] = '1'
    else:
        B[i] = '0'
    max_val = max(int(''.join(A)) - int(''.join(B)), max_val)
    B[i] = tmp
print(max_val)