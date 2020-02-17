N = int(input())
A = list(map(int,input().split()))
for a in A:
    if a % 2 == 1:
        continue
    if a % 3 != 0 and a % 5 != 0:
        print("DENIED")
        exit()
print("APPROVED")
