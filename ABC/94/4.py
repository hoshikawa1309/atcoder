N = int(input())
A = list(map(int,input().split()))
A.sort(reverse=True)
max_val = A[0]
min_val = float("inf")
for i in range(1,N):
    tmp_min = abs(max_val / 2 - A[i])
    if min_val > tmp_min:
        min_val = tmp_min
        ans_min = A[i]
print(max_val , ans_min)