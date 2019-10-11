def gcd(x , y):
    while y != 0:
        x , y = y , x%y
    return x


A , B , K = map(int,input().split())

lst = []
for i in range(1,max(A,B) + 1):
    if (A / i).is_integer() and (B / i).is_integer():
       lst.append(i)
lst.sort(reverse=True)
print(lst[K - 1])
#print(lst)