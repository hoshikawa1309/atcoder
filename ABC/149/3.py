def make_divisors(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

x = int(input())
while True:
    if make_divisors(x):
        print(x)
        exit()
    x += 1