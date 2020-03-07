N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
a_odd = 0
a_even = 0
b_odd = 0
b_even = 0
for i in range(N):
    if A[i] % 2 == 0:
        a_odd += 1
    else:
        a_even += 1
    if B[i] % 2 == 0:
        b_odd += 1
    else:
        b_even += 1
if a_odd == b_odd:
    print("Yes")
else:
    print("No")

