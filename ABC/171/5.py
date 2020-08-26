N = int(input())
scarfs = list(map(int, input().split()))
xor_sum = scarfs[0]
for i in range(1, N):
    xor_sum = xor_sum ^ scarfs[i]

for scarf in scarfs:
    print(xor_sum ^ scarf, end=' ')
