X , Y , Z , K = map(int ,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
ab_value = []
value = []
flag = False

for a in A:
    for b in B:
        ab_value.append(a + b)

ab_value.sort(reverse = True)
ab_value = ab_value[:K + 1]
C.sort(reverse = True)
i = 0
for k in ab_value:
    for c in C:
        value.append(c + k)
value.sort(reverse= True)
for i in range(K):
    print(value[i])