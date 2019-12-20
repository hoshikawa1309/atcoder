N = int(input())
N = N % 30
num = ["1","2","3","4","5","6"]
for i in range(N):
    idx = i % 5
    num[idx] , num[idx + 1] = num[idx + 1] , num[idx]
print("".join(num))