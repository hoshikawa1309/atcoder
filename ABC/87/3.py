N = int(input())
A1 = list(map(int,input().split()))
A2 = list(map(int,input().split()))
tmp_sum = 0
sum_val = 0
for i in range(N):
    A2_sum = sum(A2[i : ])
    A1_sum = sum(A1[: i + 1])
    tmp_sum = A2_sum + A1_sum
    if tmp_sum > sum_val:
        sum_val = tmp_sum
print(sum_val)