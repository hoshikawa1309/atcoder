N = int(input())
N = 1000 - N
count = 0
coins = [500,100,50,10,5,1]
for c in coins:
    count += N // c
    N %= c
print(count)
'''

while N >= 500:
    N = N - 500
    count += 1

while N >= 100:
    N = N - 100
    count += 1

while N >= 50:
    N = N - 50
    count += 1

while N >= 10 :
    N = N - 10
    count += 1
while N >= 5 :
    N = N - 5
    count += 1

while N >= 1:
    N = N - 1
    count += 1
print(count)
'''