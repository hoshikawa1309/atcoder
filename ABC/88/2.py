N = int(input())
A = list(map(int,input().split()))
A.sort(reverse=True)
Alice = A[::2]
Bob = A[1::2]
print(sum(Alice) - sum(Bob))